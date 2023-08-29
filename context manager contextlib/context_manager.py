"""
This new keyword allows a developer to create context managers. But wait!
What’s a context manager? They are handy constructs that allow us to set
something up and tear something down automatically. For example, we might want
to open a file, write a bunch of stuff to it and then close it.
The way this works under the covers is by using some of Python’s magic methods:
 __enter__ and __exit__.
"""
import sqlite3


class DataConn:
    """"""

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    def __enter__(self):
        """
        Open the database connection
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection
        """
        self.conn.close()
        if exc_val:
            raise


if __name__ == "__main__":
    db = "test.db"
    with DataConn(db) as conn:
        cursor = conn.cursor()
