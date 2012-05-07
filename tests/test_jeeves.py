# -*- coding: utf-8 -*-

import os
import unittest

os.environ.setdefault("JEEVES_SETTINGS_MODULE", "jeeves.conf.project_template.settings")
from jeeves.conf import settings
from jeeves.core.bot import BotFactory
from jeeves.core.cache import get_cache

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
            'jeeves.contrib.plugins.shortener.ShortenPlugin',
        ]
        self.bot.handler.load_plugins()
        self.assertEqual(2, len(self.bot.handler._command_plugins))

"""
    A common set of tests that should apply to all Cache Backends
"""
class BaseCacheTestSuite(object):

    def test_simple(self):
        self.cache.set('test', 'value')
        self.assertEquals(self.cache.get('test'), 'value')

    def test_non_existent(self):
        self.assertEquals(self.cache.get('non_existent'), None)
        self.assertEquals(self.cache.get('non_existent', 'hello!'), 'hello!')

    def test_delete(self):
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        self.assertEquals(self.cache.get('key1'), 'value1')
        self.cache.delete('key1')
        self.assertEquals(self.cache.get('key1'), None)
        self.assertEquals(self.cache.get('key2'), 'value2')

    def test_unicode(self):
        stuff = {
            u'ascii': u'ascii_value',
            u'unicode_ascii': u'Iñtërnâtiônàlizætiøn1',
            u'Iñtërnâtiônàlizætiøn': u'Iñtërnâtiônàlizætiøn2',
            u'ascii2': {u'x': 1}
            }

        for (key, value) in stuff.items():
            self.cache.set(key, value)
            self.assertEquals(self.cache.get(key), value)

        for key in stuff:
            self.cache.delete(key)
            self.assertEquals(self.cache.get(key), None)

    def test_increment(self):
        self.cache.set('incr', 1)
        self.cache.incr('incr')
        self.assertEquals(self.cache.get('incr'), 2)
        self.cache.incr('incr', 10)
        self.assertEquals(self.cache.get('incr'), 12)
        self.assertRaises(ValueError, self.cache.incr, 'non_existent_key')

    def test_decrement(self):
        self.cache.set('decr', 43)
        self.cache.decr('decr')
        self.assertEquals(self.cache.get('decr'), 42)
        self.cache.decr('decr', 10)
        self.assertEquals(self.cache.get('decr'), 32)

    def tearDown(self):
        self.cache.clear()

class LocalMemCacheTestSuite(BaseCacheTestSuite, unittest.TestCase):

    def setUp(self):
        self.cache = get_cache('jeeves.core.cache.backends.localmem.LocalMemCache')

class MemCacheTestSuite(BaseCacheTestSuite, unittest.TestCase):

    def setUp(self):
        settings.CACHE_LOCATION = '127.0.0.1:11211'
        self.cache = get_cache('jeeves.core.cache.backends.memcached.MemCache')

    def test_invalid_keys(self):
        # Memcached can't have whitespace in keys
        self.assertRaises(Exception, self.cache.set, 'a key with whitespace', 'value')
        self.assertRaises(Exception, self.cache.set, 'a' * 251, 'value')

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
