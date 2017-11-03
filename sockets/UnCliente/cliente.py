import socket

host = "localhost"
port = 5000

while(1):
    socket1 = socket.socket()
    socket1.connect((host,port))
    oracion = raw_input("Ingrese texto: ")
    socket1.send(oracion)
    numero = socket1.recv(1024)
    print "Texto: ", oracion, "tiene: ", numero, "caracteres"

socket1.close()
