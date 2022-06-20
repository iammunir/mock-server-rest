import sqlite3

def insert_data(data):
    try:
        conn = sqlite3.connect('mocks.db')
        c = conn.cursor()

        columns = ""
        tags = ""
        params = []
        for k, v in data.items():
            columns = columns + k + ","
            tags = tags + "?,"
            params.append(v)
        
        columns = columns.rstrip(",")
        tags = tags.rstrip(",")

        query = "INSERT INTO mocks ({}) VALUES ({})".format(columns, tags)

        c.execute(query, tuple(params))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        raise e


def get_mock_response(data):
    try:
        conn = sqlite3.connect('mocks.db')
        conn.set_trace_callback(print)
        c = conn.cursor()
        
        where = ""
        params = []
        for k, v in data.items():
            where = where + k + " = ? AND "
            params.append(v)
        
        where = where.rstrip("AND ")

        query = "SELECT * FROM mocks WHERE {}".format(where)
        res = c.execute(query, tuple(params))
        data = res.fetchone()
        conn.close()
        return data

    except Exception as e:
        print('error executing database query')
        raise e