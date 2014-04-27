import panipuri
import sqlite3
import pickle

class SQLiteCache(panipuri.CacheBackend):
    def __init__(self, filename, tablename):
        self._db = sqlite3.connect(filename)
        self._tablename = tablename
        self._create_table()

    def _create_table(self):
        try:
            c = self._db.cursor()
            c.execute("""CREATE TABLE """ + self._tablename + """ (
            key TEXT PRIMARY KEY,
            value TEXT
            );
            """)
            self._db.commit()
            c.close()
        except sqlite3.OperationalError, e:
            pass

    def put(self, key, val):
        pickled_val = pickle.dumps(val)
        c = self._db.cursor()
        c.execute("INSERT INTO " + self._tablename  + " (key, value) VALUES (?,?);", (key, pickled_val))
        self._db.commit()

    def get(self, key):
        c = self._db.cursor()
        c.execute("SELECT value FROM " + self._tablename + " WHERE key=?;", (key,))
        pickled_value = c.fetchone()
        if (pickled_value is None):
            raise KeyError("key " + key + " not found")
        c.close()
        return pickle.loads(pickled_value[0])
