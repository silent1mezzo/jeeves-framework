import os
import unittest
import mock

os.environ.setdefault("JEEVES_SETTINGS_MODULE", "jeeves.conf.project_template.settings")
from jeeves.conf import settings
from jeeves.core.bot import BotFactory
from jeeves.core.exceptions import JeevesException, ImproperlyConfigured

CHANNEL = "#test"
USERNAME = "tester"

"""
    Test Suite for Jeeves bot
"""
class JeevesTestSuite(unittest.TestCase):

    def setUp(self):
        super(JeevesTestSuite, self).setUp()
        factory = BotFactory(settings)
        self.bot = factory.buildProtocol(None)


"""
    Test Suite for Jeeves Plugins
"""
class PluginsTestSuite(unittest.TestCase):
    def setUp(self):
        super(PluginsTestSuite, self).setUp()
        factory = BotFactory(CHANNEL, USERNAME, None)
        self.bot = factory.buildProtocol(None)

    def test_load(self):
        settings.PLUGINS = [
            'tests.plugin_test.ExampleGenericPlugin',
            'tests.plugin_test.ExampleCommandPlugin',
        ]

        self.bot.handler.load_plugins()
        self.assertEqual(1, len(self.bot.handler._command_plugins))
        self.assertEqual(1, len(self.bot.handler._generic_plugins))

    def test_help(self):
        settings.PLUGINS = [
            'jeeves.core.plugins.admin.HelpPlugin',
        ]

        self.bot.handler.load_plugins()
        self.assertEqual(2, len(self.bot.handler._command_plugins))

    def test_shortener(self):
        settings.PLUGINS = [
            'jeeves.core.plugins.shortener.ShortenPlugin',
        ]
        self.bot.handler.load_plugins()
        self.assertEqual(2, len(self.bot.handler._command_plugins))

"""
    Test Suite for Jeeves.conf.settings
"""
class SettingsTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def test_override(self):
        settings.TEST = 'test'
        self.assertEqual('test', settings.TEST)
        del settings.TEST

    def test_settings_delete(self):
        settings.TEST = 'test'
        self.assertEqual('test', settings.TEST)
        del settings.TEST
        self.assertRaises(AttributeError, getattr, settings, 'TEST')

if __name__ == '__main__':
    unittest.main()
