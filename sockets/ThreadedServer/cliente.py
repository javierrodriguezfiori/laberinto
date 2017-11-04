import socket
from settings import *
import pickle

def main():
    mensaje = ""
    print "Cliente 1.0"
    sock = socket.socket()
    sock.connect((host,port))
    while mensaje != "salir":
        mensaje = raw_input ("Mensaje: ")
        try:
            sock.sendall(mensaje)
        except:
            print "No se pudo enviar el mensaje"
        try:
            data = sock.recv(4096)
            data_string = pickle.loads(data)
            print data_string
        except:
            print "No se pudo recibir respuesta"
    sock.close()

main()
