from jeeves.core.cache.backends.base import BaseCache

class MemCache(BaseCache):
    import memcache

    def __init__(self, server, params):
        BaseCache.__init__(self, params)
        global _cache
        self._cache = self.memcache.Client([server])

    def set(self, key, value):
        key = self.make_key(key)

        self._cache.set(key, value)

    def get(self, key, default=None):
        key = self.make_key(key)

        value = self._cache.get(key)

        if value == None:
            value = default

        return value

    def incr(self, key, delta=1):
        key = self.make_key(key)

        try:
            value = self._cache.incr(key, delta)
        except self.pylibmc.NotFound:
            value = None

        if value == None:
            raise ValueError("Key '%s' not found" % key)

        return value

    def decr(self, key, delta=1):
        key = self.make_key(key)

        try:
            value = self._cache.decr(key, delta)
        except Exception:
            value = None

        if value == None:
            raise ValueError("Key '%s' not found" % key)

        return value

    def delete(self, key):
        key = self.make_key(key)
        self._cache.delete(key)

    def clear(self):
        self._cache.flush_all()

