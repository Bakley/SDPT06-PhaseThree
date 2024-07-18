import sqlite3
import os

DATABASE_FILE = os.path.join(os.path.dirname(__file__), 'library.db')

def setup_database():
    connector = sqlite3.connect(DATABASE_FILE)
    cursor = connector.cursor()

    with open('sql/database.sql', 'r') as f:
        schema_script = f.read()
        cursor.executescript(schema_script)

    connector.commit()
    connector.close()

def execute_query(query, params=None, fetch_all=True):
    conn = sqlite3.connect(DATABASE_FILE)
    cur = conn.cursor()

    if params:
        cur.execute(query, params)
    else:
        # import pdb; pdb.set_trace()
        cur.execute(query)

    if fetch_all:
        result = cur.fetchall()
    else:
        result = cur.fetchone()

    conn.commit()
    conn.close()

    return result
