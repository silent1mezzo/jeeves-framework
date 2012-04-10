from jeeves.core.plugin import CommandPlugin

"""
    Shorten Plugin.
    A basic Jeeves plugin that displays help messages for the user. T
"""
class ShortenPlugin(CommandPlugin):
    name = 'Shorten Plugin'
    command = ['shorten', '-s']

    def __init__(self, *args, **kwargs):
        super(ShortenPlugin, self).__init__(self.name, self.command, *args, **kwargs)

    def handle_message(self, channel, nickname, message, command):
        tokenized_msg = message.split()
        if len(tokenized_msg) != 1:
            self.say(channel, "%s: %s" % (nickname, self.help_text))
        else:
            self.say(channel, "Shortening %s" % message)
            
    @property
    def help_text(self):
        help_text = [
            "usage: Jeeves: [shorten|-s] <link>",
        ]

        return help_text
