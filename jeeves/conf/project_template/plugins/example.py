from jeeves.core.plugin import CommandPlugin, GenericPlugin

class ExampleGenericPlugin(GenericPlugin):
    name = 'Example Generic Plugin'

    def __init__(self, *args, **kwargs):
        super(ExampleGenericPlugin, self).__init__(self.name, *args, **kwargs)

    def handle_message(self, channel, message):
        self.say(channel, "I am a Generic Plugin")

class ExampleCommandPlugin(CommandPlugin):
    name = 'Example Command Plugin'
    command = 'example'

    def __init__(self, *args, **kwargs):
        super(Google, self).__init__(self.name, self.command, *args, **kwargs)

    def handle_message(self, channel, message):
        self.say(channel, "I am a Command Plugin")
