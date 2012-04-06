from jeeves.core.plugin import CommandPlugin, GenericPlugin

class CopyCat(GenericPlugin):
    name = 'CopyCat'

    def __init__(self, *args, **kwargs):
        super(CopyCat, self).__init__(self.name, *args, **kwargs)

    def handle_message(self, channel, message):
        pass

class Google(CommandPlugin):
    name = 'Google'
    command = 'google'

    def __init__(self, *args, **kwargs):
        super(Google, self).__init__(self.name, self.command, *args, **kwargs)

    def handle_message(self, channel, message):
        self.say(channel, "Running Google Command")
