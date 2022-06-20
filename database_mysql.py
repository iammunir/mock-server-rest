import pymysql
from repository_mysql import mysql_connection

conn = mysql_connection()
c = conn.cursor()

query = """
    CREATE TABLE mocks (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        method  VARCHAR(10),
        path    VARCHAR(255),
        headers_req TEXT,
        body_req    TEXT,
        status_code VARCHAR(10),
        headers_res TEXT,
        body_res    TEXT
    );
"""

c.execute(query)

conn.commit()

conn.close()