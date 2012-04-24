from jeeves.core.cache.backends.base import BaseCache
try:
    import cPickle as pickle
except ImportError:
    import pickle

_cache = {}

class LocalMemCache(BaseCache):
    def __init__(self, name, params):
        BaseCache.__init__(self, params)
        global _cache
        self._cache = _cache

    def set(self, key, value):
        key = self.make_key(key)
        pickled = pickle.dumps(value, pickle.HIGHEST_PROTOCOL)
        self._cache[key] = pickled

    def get(self, key, default=None):
        key = self.make_key(key)
        try:
            pickled = self._cache[key]
            return pickle.loads(pickled)
        except (pickle.PickleError, KeyError):
            return default

    def incr(self, key, delta=1):
        key = self.make_key(key)
        value = self.get(key)

        if value is None:
            raise ValueError("Key '%s' not found" % key)

        new_value = value + delta
        self.set(key, new_value)

        return new_value

    def delete(self, key):
        key = self.make_key(key)
        try:
            del self._cache[key]
        except KeyError:
            pass

    def clear(self):
        self._cache.clear()
