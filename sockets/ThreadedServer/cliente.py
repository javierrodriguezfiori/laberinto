import socket
from settings import *
import pickle

def request_map():
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
            try:
                data_string = pickle.loads(data)
                print data_string
            except:
                print(data)
        except:
            print "No se pudo recibir data"
    sock.close()

main()
