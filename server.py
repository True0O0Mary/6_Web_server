import socket
import os
import threading
from settings import PORT, WORKING_DIR, REQUEST_SIZE
from check import code_request
# WORKING_DIR = os.getcwd()
# PORT = 80

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', PORT))
server.listen(5)

if __name__ == "__main__":
    while True:
        conn, addr = server.accept()
        print(addr)
        request = conn.recv(REQUEST_SIZE).decode().split("\n")
        # print(request)

        method, url, protocol = request[0].split(" ")
        url = os.path.join(WORKING_DIR, url[1:])
        print(url)



        if os.path.isdir(url):
            url = os.path.join(url, "index.htm")

        code, body = code_request(url)

        response = f"HTTP/1.1 {code}\n"
        response += "Server my_dummy_server\n"
        response += "\n"
        response += f"{body}"
        conn.send(response.encode())
        conn.close()
        print("Connection closed")

# while True:
#
#     conn, addr = server.accept()
#     print("Connected", addr)
#
#     request = conn.recv(8192).decode().split('\n')
#
#     method, url, protocol = request[0].split(' ')
#     print(url)
#     url = os.path.join(WORKING_DIR, url[1:])
#     print(url)
#
#     code = "404 Not Found"
#     body = ""
#     url = os.path.join(url, 'index.htm')
#     if os.path.isfile(url):
#         code = "200 OK"
#         body = open(url, 'r').read()
#         print(f"Body: {body}")
#
#     resp = f'HTTP/1.1 {code}\n'
#     resp += "Server: my_dummy_server"
#     resp += '\n\n'
#     resp += body
#     conn.send(resp.encode())
#     conn.close()
#     print('Connection closed\n')