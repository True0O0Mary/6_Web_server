import os
import re
allowed_extensions = ["htm", "html", "css"]

def code_request(url):
    body=""
    if check_file_type(url):
        if os.path.exists(url):
            body = open(url, "r").read()
            return "200 OK", body
        return "404 Not Found", body
    return "403 Forbidden", body


def check_file_type(url):
    if url[-1] == "/" or url.split(".")[-1] in allowed_extensions:
        return True
    return False