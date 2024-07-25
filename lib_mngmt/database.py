import sqlite3

class Database:
    """
    This file will handle database connections 
    and query execution.
    """
    def __init__(self, db_name="lib.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        # import pdb; pdb.set_trace()
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchone(self):
        return self.cursor.fetchone()
    
    def fetchall(self):
        return self.cursor.fetchall()

db = Database()
