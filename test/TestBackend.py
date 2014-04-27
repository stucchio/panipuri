import unittest
from panipuri import *
from panipuri.backends import *
import tempfile
import shutil
import os

class DummyCache(object):
    def __init__(self):
        self.dict = {}

    def put(self, key, val):
        self.dict[key]=val

    def get(self, key):
        return self.dict[key]

class AbstractTestCacheBackend(unittest.TestCase):

    def setUp(self):
        """
        Override this to create the self.cache variable.
        """
        self.cache = DummyCache()

    def test_put_get(self):
        self.cache.put("foo", "bar")
        self.assertEqual(self.cache.get("foo"), "bar")

    def test_key_error(self):
        def _should_throw(cache):
            return cache.get("missing")
        # should raise an exception for an immutable sequence
        self.assertRaises(KeyError, _should_throw, self.cache )

class TestSQLiteCache(AbstractTestCacheBackend):
    def setUp(self):
        self.cache = SQLiteCache("", "test_table")

class TestDBMCache(AbstractTestCacheBackend):
    def setUp(self):
        self.dir = tempfile.mkdtemp(dir="/tmp")
        self.cache = DBMCache(os.path.join(self.dir, "testdbmcache"))

    def tearDown(self):
        self.cache.close()
        shutil.rmtree(self.dir)

if __name__ == '__main__':
    unittest.main()
