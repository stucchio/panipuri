class CacheBackend(object):
    def put(self, key, val):
        raise NotImplemented

    def get(self, key):
        raise NotImplemented

def default_keyfunc(*args, **kwargs):
    return str([args, kwargs])

class PanipuriFunc(object):
    def __init__(self, func, cache, keyfunc=default_keyfunc):
        self._func = func
        self._keyfunc = keyfunc
        self._cache = cache

    def __call__(self, *args, **kwargs):
        key = self._keyfunc(*args, **kwargs)
        try:
            return self._cache.get(key)
        except KeyError:
            val = self._func(*args, **kwargs)
            self._cache.put(key, val)
            return val
