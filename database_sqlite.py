import sqlite3

conn = sqlite3.connect('mocks.db')
c = conn.cursor()

query = """
    CREATE TABLE mocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        method  TEXT,
        path    TEXT,
        headers_req TEXT,
        body_req    TEXT,
        status_code TEXT,
        headers_res TEXT,
        body_res    TEXT
    );
"""

c.execute(query)

conn.commit()

conn.close()