import sys
import threading
import Pyro4

#
# if sys.version_info < (3, 0):
#     input = raw_input


# The daemon is running in its own thread, to be able to deal with server
# callback messages while the main thread is processing user input.


class Chatter(object):
    def __init__(self):
        self.chatbox = Pyro4.core.Proxy('PYRONAME:example.chatbox.server')
        self.abort = 0

    @Pyro4.expose
    @Pyro4.oneway
    def message(self, nick, msg):
        if nick != self.nick:
            print('[{0}] {1}'.format(nick, msg))

    def start(self):
        while True:
            nicks = self.chatbox.getNicks()
            if nicks:
                print('The following people are on the server: %s' % (', '.join(nicks)))
            channels = sorted(self.chatbox.getChannels())
            if channels:
                print('The following channels already exist: %s' % (', '.join(channels)))
                self.channel = input('Choose a channel or create a new one: ').strip()
            else:
                print('The server has no active channels.')
                self.channel = input('Name for new channel: ').strip()
            self.nick = input('Choose a nickname: ').strip()
            result = self.chatbox.join(self.channel, self.nick, self)
            if isinstance(result, str):
                print(result)  # Show the error message
                continue
            else:
                break

        people = result
        print('Joined channel %s as %s' % (self.channel, self.nick))
        print('People on this channel: %s' % (', '.join(people)))
        print('Ready for input! Type /quit to quit, /add <nick> to add permission, /dm <nick> <message> to DM someone')
        try:
            try:
                while not self.abort:
                    line = input('> ').strip()
                    if line == '/quit':
                        self.chatbox.leave(self.channel, self.nick)
                        self.start()
                    elif line.startswith('/add '):
                        nick_to_add = line.split()[1]
                        message = self.chatbox.add_permission(self.channel, self.nick, nick_to_add)
                        print(message)
                    elif line.startswith('/dm '):
                        parts = line.split(' ', 2)
                        if len(parts) >= 3:
                            nick_to_dm = parts[1]
                            dm_message = parts[2]
                            result = self.chatbox.send_dm(self.nick, nick_to_dm, dm_message)
                            print(result)
                        else:
                            print("Invalid DM format. Use: /dm <nick> <message>")
                    elif line:
                        self.chatbox.publish(self.channel, self.nick, line)
            except EOFError:
                pass
        finally:
            self.chatbox.leave(self.channel, self.nick)
            self.abort = 1
            self._pyroDaemon.shutdown()


class DaemonThread(threading.Thread):
    def __init__(self, chatter):
        threading.Thread.__init__(self)
        self.chatter = chatter
        self.setDaemon(True)

    def run(self):
        with Pyro4.core.Daemon() as daemon:
            daemon.register(self.chatter)
            daemon.requestLoop(lambda: not self.chatter.abort)


chatter = Chatter()
daemonthread = DaemonThread(chatter)
daemonthread.start()
chatter.start()
print('Exit.')
