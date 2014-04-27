from backends import DBMCache

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

def simple_cache(filename):
    cache = DBMCache(filename)
    def _wrapper(func):
        ppf = PanipuriFunc(func, cache)
        return ppf
    return _wrapper
