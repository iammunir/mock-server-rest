IGNORED_HEADERS = ['User-Agent', 'Accept', 'Postman-Token', 'Host', 'Accept-Encoding', 'Connection', 'Content-Length', 'Content-Type']

def process_headers(ori_headers):
    headers_obj = {}
    for k, v in ori_headers.items():
        if k not in IGNORED_HEADERS:
            headers_obj[k] = v
    keys = headers_obj.keys()
    keys = list(sorted(keys))
    sorted_obj = {}
    for k in keys:
        sorted_obj[k.lower()] = headers_obj[k]
    return sorted_obj

