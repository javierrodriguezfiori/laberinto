import socket
import sys
from thread import *

host = ''
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

try:
    s.bind((host,port))
except socket.error:
    print("Binding failed")
    sys.exit()

print("Socket has been bounded")

s.listen(10)

print("Socket is ready")

def client_thread(conn):
    conn.send("Welcome. Type something and hit enter:\n")
    while True:
        data = conn.recv(1024)
        reply = "OK. "+data
        if not data:
            break
        print(reply)
        conn.sendall(data)
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected width "+addr[0]+":"+str(addr[1]))
    start_new_thread(client_thread, (conn,))

s.close()
