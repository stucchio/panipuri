from CacheBackend import CacheBackend
import os

class FilesystemDataframeCache(CacheBackend):
    """
    A backend for caching dataframes *only*. No other types will work.

    Pandas must be available if you use this backend.
    """
    import pandas

    def __init__(self, filename):
        self._datadir = filename
        try:
            os.makedirs(self._datadir)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(self._datadir):
                pass
            else: raise

    def _path(self, key):
        return os.path.join(self._datadir, key)

    def put(self, key, val):
        if type(val) == self.pandas.DataFrame:
            val.to_csv(self._path(key))
        else:
            raise ValueError("This cache can only handle dataframes. You passed in a " + str(type(val)))

    def get(self, key):
        try:
            df = self.pandas.read_csv(self._path(key))
            return df
        except IOError, e:
            raise KeyError("key " + key + " not found")
