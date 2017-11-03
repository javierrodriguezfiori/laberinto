import socket

def main():
    mensaje = ""
    print "Cliente 1.0"
    host, port = "localhost" , 5000
    sock = socket.socket()
    sock.connect((host,port))
    while mensaje != "salir":
        print "Ingrese mensaje o salir para terminar"
        mensaje = raw_input ("Mensaje: ")
        try:
            sock.send(mensaje)
        except:
            print "No se pudo establecer la conexion con el servidor"
    sock.close()

main()
