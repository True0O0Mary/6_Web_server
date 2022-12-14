import socket

# HOST = "10.0.2.15"
HOST ="google.com"
PORT = 80


web = socket.socket()
web.connect((HOST, PORT))

msg = """GET / HTTP/1.1
Host: www.google.com

"""

web.send(msg.encode())
response = web.recv(1024).decode()
web.close()
print(response)