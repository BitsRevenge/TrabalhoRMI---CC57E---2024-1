import os
import shutil
import sys
import threading
import Pyro4

#
# if sys.version_info < (3, 0):
#     input = raw_input


# The daemon is running in its own thread, to be able to deal with server
# callback messages while the main thread is processing user input.

#A fazer:
#Envio de arquivos: em chats privados, um usuário poderá enviar arquivos ao outro usuário.

#Exclusão: um usuário poderá requisitar ao servidor que um usuário seja banido da aplicação. Banir um usuário do grupo
# é tarefa do administrador do grupo. Caso o administrador do grupo saia, o aplicativo deve decidir quem será o
# novo administrador, ou se o grupo seja eliminado. Tal opção pode ser ajustada no momento da criação do chat em grupo.

class Chatter(object):
    def __init__(self):
        ns = Pyro4.locateNS(host="26.16.105.211", port=9090)
        uri = ns.lookup("example.service")
        self.chatbox = Pyro4.core.Proxy(uri)
        self.abort = 0

    @Pyro4.expose
    def message(self, nick, msg):
        if nick != self.nick:
            print('[{0}] {1}'.format(nick, msg))

    def start(self):
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
        people = self.chatbox.join(self.channel, self.nick, self)
        print('Joined channel %s as %s' % (self.channel, self.nick))
        # print('People on this channel: %s' % (', '.join(people)))
        print('Ready for input! Type /quit to quit and /upload to sand an archive')
        try:
            try:
                while not self.abort:
                    line = input('> ').strip()
                    if line == '/quit':
                        break
                    if line.startswith('/upload '):
                        self.chatbox.upload(self.channel, self.nick, line)
                    if line.startswith('/download '):
                        self.chatbox.download(self.channel, self.nick, line)
                    if line.startswith('/ban '):
                        print('A')
                    if line:
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
        self.daemon = True
        #self.setDaemon(True)

    def run(self):
        with Pyro4.core.Daemon() as daemon:
            daemon.register(self.chatter)
            daemon.requestLoop(lambda: not self.chatter.abort)


chatter = Chatter()
daemonthread = DaemonThread(chatter)
daemonthread.start()
chatter.start()
print('Exit.')
