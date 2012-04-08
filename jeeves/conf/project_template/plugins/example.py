from jeeves.core.plugin import CommandPlugin, GenericPlugin

class ExampleGenericPlugin(GenericPlugin):
    name = 'Example Generic Plugin'
    help_text = 'This is the help text for a generic plugin.'

    def __init__(self, *args, **kwargs):
        super(ExampleGenericPlugin, self).__init__(self.name, *args, **kwargs)

    def handle_message(self, channel, message):
        self.say(channel, "I am a Generic Plugin")

class ExampleCommandPlugin(CommandPlugin):
    name = 'Example Command Plugin'
    help_text = 'This is the help text for a command plugin.'
    command = ['example', ]

    def __init__(self, *args, **kwargs):
        super(ExampleCommandPlugin, self).__init__(self.name, self.command, *args, **kwargs)

    def handle_message(self, channel, message):
        self.say(channel, "I am a Command Plugin")
