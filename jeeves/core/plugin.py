from jeeves.core import exceptions

class Plugin(object):
    help_text = ''

    def __init__(self, **kwargs):
        self.protocol = kwargs['protocol']

    def handle_message(self, channel, nick, msg):
        raise exceptions.NotImplemented('Plugin %s must implement handle_message()' % self.__class__)

    def say(self, channel, msg):
        self.protocol.msg(channel, msg)

    @property
    def help_text(self):
        return self.help_text

    @property
    def name(self):
        return self.name

    @property
    def command(self):
        return self.command

'''
    Generic Plugin

    Runs on every message sent to a channel.
    e.g. A plugin that logs every message, A plugin that is triggered off specific sayings
'''
class GenericPlugin(Plugin):
    def __init__(self, name, **kwargs):
        super(GenericPlugin, self).__init__(**kwargs)

'''
    Command Plugin

    Runs only when mesages are directed to the bot (either private or not).
    e.g. you: <botname> define "pedantic" would return the definition for the word pedantic
'''
class CommandPlugin(Plugin):
    def __init__(self, name, command, **kwargs):
        super(CommandPlugin, self).__init__(**kwargs)
