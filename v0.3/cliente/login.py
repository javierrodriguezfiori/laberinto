import socket
import pickle
import sys

def login(usuario, password):
    resultado = 0
    try:
        sock = socket.socket()
        sock.connect((host,port))
        try:
            peticion = pickle.dumps(["login",usuario,password])
            sock.sendall(peticion)
        except:
            print "No se pudo enviar la peticion"
        try:
            data = sock.recv(1024)
            data_string = pickle.loads(data)
            if(data_string=="ok"):
                resultado = 1
            else:
                if(data_string=="error"):
                    resultado = 2
        except:
            print("No se pudo recibir el mapa")
    except:
        print("No se pudo contactar al servidor")
        sys.exit()
    return resultado
