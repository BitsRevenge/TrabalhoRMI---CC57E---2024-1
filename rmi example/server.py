import Pyro4


# Chat box administration server.
# Handles logins, logouts, channels and nicknames, and the chatting.
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class ChatBox(object):
    def __init__(self):
        self.channels = {}  # registered channels { channel --> (nick, client callback) list }
        self.nicks = {}  # all registered nicks on this server {nick: callback}
        self.channel_owners = {}  # channel owners { channel: nick }
        self.channel_permissions = {}  # channel permissions { channel: [nicks] }
        self.dm_channels = {}

    def getChannels(self):
        return list(self.channels.keys())

    def getNicks(self):
        return list(self.nicks.keys())

    def join(self, channel, nick, callback):
        if not channel or not nick:
            return "Invalid channel or nick name."
        if nick in self.nicks:
            return "This nick is already in use."
        if channel not in self.channels:
            print('CREATING NEW CHANNEL %s' % channel)
            self.channels[channel] = []
            self.channel_owners[channel] = nick  # Set the creator as the owner
            self.channel_permissions[channel] = [nick]  # Creator has permission
        elif nick not in self.channel_permissions[channel]:
            return "You do not have permission to join this channel."
        
        self.channels[channel].append((nick, callback))
        self.nicks[nick] = callback
        print("%s JOINED %s" % (nick, channel))
        self.publish(channel, 'SERVER', '** ' + nick + ' joined **')
        return [nick for (nick, c) in self.channels[channel]]  # return all nicks in this channel

    def leave(self, channel, nick):
        if channel not in self.channels:
            print('IGNORED UNKNOWN CHANNEL %s' % channel)
            return
        for (n, c) in self.channels[channel]:
            if n == nick:
                self.channels[channel].remove((n, c))
                break
        self.publish(channel, 'SERVER', '** ' + nick + ' left **')
        if len(self.channels[channel]) < 1:
            del self.channels[channel]
            del self.channel_owners[channel]  # Remove the owner when the channel is empty
            del self.channel_permissions[channel]  # Remove permissions
            print('REMOVED CHANNEL %s' % channel)
        del self.nicks[nick]
        print("%s LEFT %s" % (nick, channel))

    def publish(self, channel, nick, msg):
        if channel not in self.channels:
            print('IGNORED UNKNOWN CHANNEL %s' % channel)
            return
        for (n, c) in self.channels[channel][:]:  # use a copy of the list
            try:
                c.message(nick, msg)  # oneway call
            except Pyro4.errors.ConnectionClosedError:
                # connection dropped, remove the listener if it's still there
                # check for existence because other thread may have killed it already
                if (n, c) in self.channels[channel]:
                    self.channels[channel].remove((n, c))
                    print('Removed dead listener %s %s' % (n, c))

    def send_dm(self, from_nick, to_nick, message):
        if to_nick not in self.nicks:
            return f"User {to_nick} not found."
        try:
            self.nicks[to_nick].message(from_nick, f"DM from {from_nick}: {message}")
        except Pyro4.errors.ConnectionClosedError:
            return f"Failed to send DM to {to_nick}."
        return f"DM sent to {to_nick}."

    def add_permission(self, channel, owner, nick_to_add):
        if channel not in self.channel_owners or self.channel_owners[channel] != owner:
            return "Only the channel owner can add permissions."
        if nick_to_add in self.channel_permissions[channel]:
            return f"{nick_to_add} already has permission."
        self.channel_permissions[channel].append(nick_to_add)
        return f"Permission added for {nick_to_add}."

if __name__ == "__main__":
    # Locate the Pyro nameserver
    try:
        ns = Pyro4.locateNS(host='localhost', port=9090)  # Ensure these match your nameserver settings
        print("Nameserver located.")
    except Pyro4.errors.NamingError as e:
        print("Failed to locate the nameserver: ", e)
        raise

    # Create a Pyro daemon
    daemon = Pyro4.Daemon()

    # Register the ChatBox object
    uri = daemon.register(ChatBox)

    # Register the object with the nameserver
    ns.register("example.chatbox.server", uri)

    print("ChatBox server is running.")

    # Start the event loop of the server to wait for calls
    daemon.requestLoop()