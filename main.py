import json
from operator import contains
from flask import Flask, make_response, request
from flask_cors import CORS

from admin import admin_function
from mock import process_headers
from repository_mysql import get_mock_response

app = Flask(__name__)
CORS(app)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route('/', methods=HTTP_METHODS, defaults={'path': ''})
@app.route('/<path:path>', methods=HTTP_METHODS)
def catch_all(path):
    try:
        method = request.method
        real_headers = request.headers

        request_body = None
        if contains(real_headers.get('content-type'), 'json'):
            request_body = request.json
        elif contains(real_headers.get('content-type'), 'form'):
            request_body = request.form

        auth = request.authorization
        if hasattr(auth, 'username') and hasattr(auth, 'password'):
            if auth['username'] == 'adminmock' and auth['password'] == 'supersecret':
                res = admin_function(method, path, request_body)
                return res

        headers_obj = process_headers(real_headers)
        headers_obj = json.dumps(headers_obj, separators=(',', ':'))
        request_body = json.dumps(request_body, separators=(',', ':'))

        data = {
            'method': method,
            'path': path,
            'headers_req': headers_obj,
            'body_req': request_body
        }

        result = get_mock_response(data)
        if result is None:
            return {'status': 'failed', 'message': 'No response is found'}
    
        status = result[0]
        headers = result[1]
        res = result[2]

        headers = json.loads(headers)
        resp = make_response(res)
        for k, v in headers.items():
            resp.headers[k] = v

        return resp, int(status)

    except Exception as e:
        return {'status': 'failed', 'message': str(e)}


if __name__ == '__main__':
    app.run(debug=True, port=30765)
