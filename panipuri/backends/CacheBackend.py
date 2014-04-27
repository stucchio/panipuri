class CacheBackend(object):
    def put(self, key, val):
        raise NotImplemented

    def get(self, key):
        raise NotImplemented
