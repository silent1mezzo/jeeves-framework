from jeeves.core.plugin import CommandPlugin

class HelpPlugin(CommandPlugin):
    name = 'Help Plugin'
    command = ['help', '-h']

    def __init__(self, *args, **kwargs):
        super(HelpPlugin, self).__init__(self.name, self.command, *args, **kwargs)

    def handle_message(self, channel, message):
        self.say(channel, "I am a Command Plugin")

    @property
    def help_text(self):
        self.say("usage: Jeeves [comand] msg")
