from jeeves.core.plugin import CommandPlugin
from jeeves.conf import settings
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
            self.say(nickname, "Here's a list of all of the available commands:")
            for key in self.handler._command_plugins.keys():
                self.say(nickname, "Jeeves: %s" % key)
        elif tokenized_msg and tokenized_msg[0] in self.handler._command_plugins.keys():
            for text in self.handler._command_plugins[tokenized_msg[0]].help_text:
                self.say(nickname, text)
        else:
            for text in self.help_text:
                self.say(nickname, text)

    @property
    def help_text(self):
        help_text = [
            "usage: %s: [help|-h] [list_commands] [command_name]" % settings.NICKNAME,
            "To list available plugins `%s: help list_commands`" % settings.NICKNAME,
            "To get specific help for a plugin `%s: help [command_name]`" % settings.NICKNAME,
        ]

        return help_text
