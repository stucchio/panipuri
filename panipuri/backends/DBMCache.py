from CacheBackend import CacheBackend
import dbm
import pickle

class DBMCache(CacheBackend):
    def __init__(self, filename):
        self._db = dbm.open(filename, 'c')

    def put(self, key, val):
        pickled_val = pickle.dumps(val)
        self._db[key] = pickled_val

    def get(self, key):
        return pickle.loads(self._db[key])

    def close(self):
        self._db.close()
