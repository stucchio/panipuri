import unittest
from panipuri import *
import tempfile
import shutil
import os

class TestSimpleWrapper(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(dir="/tmp")
        self.cache = DBMCache(os.path.join(self.dir, "testdbmcache"))

    def test_simple_cache(self):
        times_called = {}
        @simple_cache(self.cache)
        def f(x):
            times_called[x] = times_called.get(x,0)+1
            return x

        self.assertEqual(f("foo"), "foo")
        self.assertEqual(f("foo"), "foo")
        self.assertEqual(f("bar"), "bar")
        self.assertEqual(f("bar"), "bar")
        self.assertEqual(times_called['foo'], 1)
        self.assertEqual(times_called['bar'], 1)

    def tearDown(self):
        self.cache.close()
        shutil.rmtree(self.dir)

if __name__ == '__main__':
    unittest.main()
