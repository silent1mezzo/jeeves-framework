from jeeves import __version__ as jeeves_version
from jeeves.conf import settings
from jeeves.core.handlers import base

from twisted.words.protocols import irc
from twisted.internet import protocol

class Bot(irc.IRCClient):
    plugins = {}

    def __init__(self):
        self.handler = base.BaseHandler(self)
        self.password = settings.SERVER_PASSWORD
        print "Jeeves version %s" % jeeves_version

    def signedOn(self):
        #Initialize Plugins
        self.handler.load_plugins()

        #Run any plugins on signon
        self.join(self.factory.channel, self.factory.password)

        #Another use already exists with the same username. Update the stored nickname to what IRC gave us
        if self.nickname != settings.NICKNAME:
            settings.NICKNAME = self.nickname
        print "Signed on as %s." % self.nickname

    def joined(self, channel):
        print "Joined %s." % channel

    def privmsg(self, user, channel, msg):
        self.handler.message(user, channel, msg)

    def irc_ERR_PASSWDMISMATCH(self, prefix, params):
        print 'wrong password'

    @property
    def nickname(self):
        return self.factory.nickname

    @property
    def channel(self):
        return self.factory.channel

class BotFactory(protocol.ClientFactory):
    protocol = Bot

    def __init__(self, channel, nickname, password):
        self.channel = channel
        self.nickname = nickname
        self.password = password

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)
