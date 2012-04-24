from jeeves.utils.encoding import smart_str

class BaseCache(object):
    def __init__(self, params):
        timeout = params.get('timeout', params.get('TIMEOUT', 300))
        try:
            timeout = int(timeout)
        except (ValueError, TypeError):
            timeout = 300

        self.default_timeout = timeout

    def make_key(self, key):
        return smart_str(key)

    def set(self, key, value):
        """Sets a value in the cache for the given key."""
        raise NotImplementedError

    def get(self, key, default=None):
        """
        Fetch a given key from the cache. If the key does not exist, return
        default, which itself defaults to None.
        """
        raise NotImplementedError

    def incr(self, key, delta=1):
        """
        Add delta to value in the cache. If the key does not exist, raise a
        ValueError exception.
        """
        raise NotImplementedError

    def decr(self, key, delta=1):
        """
        Subtract delta from value in the cache. If the key does not exist, raise
        a ValueError exception.
        """
        return self.incr(key, -delta)

    def delete(self, key):
        """Remove a given key from the cache."""
        raise NotImplementedError

    def clear(self):
        """Remove *all* values from the cache at once."""
        raise NotImplementedError
