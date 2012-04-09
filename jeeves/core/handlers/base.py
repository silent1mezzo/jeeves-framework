from jeeves.conf import settings
from jeeves.core import exceptions
from jeeves.utils import importlib, utils

class BaseHandler(object):
    def __init__(self, protocol=None):
        self.protocol = protocol

        self._command_plugins = []
        self._commands = {}
        self._generic_plugins = []

    def load_plugins(self):
        """
        Populate plugin lists from settings.PLUGINS.

        """

        for plugin_path in settings.PLUGINS:
            try:
                pg_module, pg_classname = plugin_path.rsplit('.', 1)
            except ValueError, e:
                raise exceptions.ImproperlyConfigured('%s isn\'t a plugin module' % plugin_path)

            try:
                mod = importlib.import_module(pg_module)
            except ImportError, e:
                raise exceptions.ImproperlyConfigured('Error importing plugin %s: "%s"' % (pg_module, e))

            try:
                pg_class = getattr(mod, pg_classname)
            except AttributeError, e:
                raise exceptions.ImproperlyConfigured('Plugins module "%s" does not define a "%s" class' % (pg_module, pg_classname))

            try:
                pg_instance = pg_class(protocol=self.protocol)
            except TypeError, e:
                raise exceptions.InvalidPlugin('Plugins class "%s" does not provide a command: %s' % (pg_class, e))

            if hasattr(pg_instance, 'command'):
                self._command_plugins.append(pg_instance)
                if isinstance(pg_instance.command, str):
                    self._commands[pg_instance.command] = pg_instance.handle_message
                else:
                    for command in pg_instance.command:
                        self._commands[command] = pg_instance.handle_message
            else:
                self._generic_plugins.append(pg_instance)

    def message(self, user, channel, msg):
        user = user.split('!', 1)[0]

        nick, command, message = utils.parse_message(msg, self._commands.keys())
        print nick, command, message
        for plugin in self._generic_plugins:
            plugin.handle_message(channel, msg)

        if nick and command:
            self._commands[command](channel, message)
