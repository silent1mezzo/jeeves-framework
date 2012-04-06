import os

from jeeves.conf import base_settings
from jeeves.utils import importlib

ENVIRONMENT_VARIABLE = "JEEVES_SETTINGS_MODULE"

class BaseSettings(object):
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

class Settings(BaseSettings):
    def __init__(self):
        # update this dict from global settings (but only for ALL_CAPS settings)
        for setting in dir(base_settings):
            if setting == setting.upper():
                setattr(self, setting, getattr(base_settings, setting))

        try:
            settings_module = os.environ[ENVIRONMENT_VARIABLE]
        except KeyError:
            raise ImportError("Settings cannot be imported, because environment variable %s is undefined." % ENVIRONMENT_VARIABLE)
        # store the settings module in case someone later cares
        self.SETTINGS_MODULE = settings_module

        try:
            mod = importlib.import_module(self.SETTINGS_MODULE)
        except ImportError, e:
            raise ImportError("Could not import settings '%s' (Is it on sys.path?): %s" % (self.SETTINGS_MODULE, e))

        for setting in dir(mod):
            if setting == setting.upper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)

settings = Settings()
