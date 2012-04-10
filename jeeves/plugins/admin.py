from jeeves.core.plugin import CommandPlugin

"""
    Help Plugin.
    A basic Jeeves plugin that displays help messages for the user. T
"""
class HelpPlugin(CommandPlugin):
    name = 'Help Plugin'
    command = ['help', '-h']

    def __init__(self, *args, **kwargs):
        super(HelpPlugin, self).__init__(self.name, self.command, *args, **kwargs)

    def handle_message(self, channel, nickname, message, command):
        tokenized_msg = message.split()

        if tokenized_msg and tokenized_msg[0] == "list_commands":
            self.say(channel, "%s: Here's a list of all of the available commands:" % nickname)
            for key in self.handler._command_plugins.keys():
                self.say(channel, "Jeeves: %s" % key)
        elif tokenized_msg and tokenized_msg[0] in self.handler._command_plugins.keys():
            for text in self.handler._command_plugins[tokenized_msg[0]].help_text:
                self.say(channel, text)
        else:
            for text in self.help_text:
                self.say(channel, text)

    @property
    def help_text(self):
        help_text = [
            "usage: Jeeves: [command] msg",
            "To list available plugins `Jeeves: help list_commands`",
            "To get specific help for a plugin `Jeeves: help [command_name]`",
        ]

        return help_text
