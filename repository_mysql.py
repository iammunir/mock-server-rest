import pymysql
import config

def mysql_connection():
    conn = pymysql.connect(db=config.DB_NAME,
                            user=config.DB_USER,
                            passwd=config.DB_PASSWORD,
                            host=config.DB_HOST,
                            port=config.DB_PORT)
    return conn

def insert_data(data):
    try:
        conn = mysql_connection()
        c = conn.cursor()

        columns = ""
        tags = ""
        params = []
        for k, v in data.items():
            columns = columns + k + ","
            tags = tags + "%s,"
            params.append(v)
        
        columns = columns.rstrip(",")
        tags = tags.rstrip(",")

        query = "INSERT INTO mocks ({}) VALUES ({})".format(columns, tags)

        c.execute(query, params)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print('error executing database execution')
        raise e


def get_mock_response(data):
    try:
        conn = mysql_connection()
        c = conn.cursor()
        
        where = ""
        params = []
        for k, v in data.items():
            where = where + k + " = %s AND "
            params.append(v)
        
        where = where.rstrip("AND ")

        query = "SELECT status_code, headers_res, body_res FROM mocks WHERE {}".format(where)
        c.execute(query, tuple(params))
        data = c.fetchone()
        conn.close()
        return data

    except Exception as e:
        print('error executing database query')
        raise e