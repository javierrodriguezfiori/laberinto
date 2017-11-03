import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to connect")
    sys.exit()

print("Socket created")

host = "www.google.com"
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

print("IP Address: "+remote_ip)

s.connect((remote_ip,port))

print("Socket connected to "+host+" using IP "+remote_ip)