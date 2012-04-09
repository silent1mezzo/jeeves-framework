import os
import unittest

os.environ.setdefault("JEEVES_SETTINGS_MODULE", "jeeves.conf.project_template.settings")
from jeeves.conf import settings
from jeeves.core.handlers import base
from jeeves.core.exceptions import InvalidPlugin, ImproperlyConfigured


"""
    Test Suite for Jeeves bot
"""
class JeevesTestSuite(unittest.TestCase):

    def setUp(self):
        pass

"""
    Test Suite for Jeeves Plugins
"""
class PluginsTestSuite(unittest.TestCase):
    def setUp(self):
        self.handler = base.BaseHandler()

    def test_load(self):
        settings.PLUGINS = [
            'jeeves.tests.plugin_test.ExampleGenericPlugin',
            'jeeves.tests.plugin_test.ExampleCommandPlugin',
        ]

        self.handler.load_plugins()
        self.assertEqual(1, len(self.handler._command_plugins))
        self.assertEqual(1, len(self.handler._generic_plugins))

        settings.PLUGINS = [
            'jeeves.tests.plugin_test.ExampleNoNamePlugin',
        ]
        self.assertRaises(InvalidPlugin, self.handler.load_plugins)

        settings.PLUGINS = [
            'jeeves.tests.plugin_test.ExampleNoCommandPlugin',
        ]
        self.assertRaises(InvalidPlugin, self.handler.load_plugins)

        settings.PLUGINS = [
            'jeeves.tests.plugin_test.NoneExistent',
        ]
        self.assertRaises(ImproperlyConfigured, self.handler.load_plugins)

        settings.PLUGINS = [
            'jeeves.tests.test.NoneExistent',
        ]
        self.assertRaises(ImproperlyConfigured, self.handler.load_plugins)

"""
    Test Suite for Jeeves.core.management
"""
class ManagementTestSuite(unittest.TestCase):
    def setUp(self):
        pass

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
