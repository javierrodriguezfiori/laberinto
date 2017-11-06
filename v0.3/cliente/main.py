import time
from game import *
from login import *
import sys
import pickle
import socket

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
            if(data=="ok"):
                resultado = 1
            else:
                if(data=="error"):
                    resultado = 2
        except:
            print("No se pudo recibir la respuesta")
    except:
        print("No se pudo contactar al servidor")
        sys.exit()
    return resultado

# Main

# Login
usuario = raw_input("Ingrese usuario: ")
password = raw_input("Ingrese password: ")

if login(usuario,password)==1:
    # Instanciar juego e iniciar el loop
    g = Game()
    while True:
        g.new()
        g.run()
        if Partida.gano:
            g.show_ganaste()
        elif Partida.perdio:
            g.show_perdiste()
        time.sleep(2)
        g.quit()
else:
    print("Error de login")
