import json
from repository_mysql import insert_data
from mock import process_headers


def create_mock(data):
    try:
        request_obj = data['request'] 
        request_body = request_obj['body']
        headers_req = request_obj['headers']
        headers_req = process_headers(headers_req)
        method = request_obj['method']
        path = request_obj['path']

        response_obj = data['response']
        status_code = response_obj['statusCode']
        headers_res = response_obj['headers']
        headers_res = process_headers(headers_res)
        response_body = response_obj['body']

        headers_req = json.dumps(headers_req, separators=(',', ':'))
        request_body = json.dumps(request_body, separators=(',', ':'))
        headers_res = json.dumps(headers_res, separators=(',', ':'))
        response_body = json.dumps(response_body, separators=(',', ':'))

        data = {
            'method': method,
            'path': path,
            'headers_req': headers_req,
            'body_req': request_body,
            'status_code': status_code,
            'headers_res': headers_res,
            'body_res': response_body
        }
        insert_data(data)
        return {'status': 'success', 'message': 'a new mock has been created'}
    except Exception as e:
        return {'status': 'failed', 'message': str(e)}


def delete_mock(data):
    pass

def edit_mock(data):
    pass

def admin_function(method, path, request_body):
    
    if method == 'POST' and path == 'create-mock':
        return create_mock(request_body)
    
    if (method == 'PUT' or method == 'UPDATE') and path == 'edit-mock':
        
        return {'status': 'success', 'message': 'selected mock has been updated'}

    if method == 'DELETE' and path == 'delete-mock':
        
        return {'status': 'success', 'message': 'selected mock has been deleted'}

    return {'status': 'failed', 'message': 'route not found'}
