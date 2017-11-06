import time
from game import *
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
            sock.send(peticion)
        except:
            print "No se pudo enviar la peticion"
        try:
            data = sock.recv(1024)
            if(data=="ok"):
                resultado = 1
            else:
                resultado = 2
        except:
            print("No se pudo recibir la respuesta")
    except:
        print("No se pudo contactar al servidor")
    return resultado

# Main

# Login
logon = False
while not logon:
    usuario = raw_input("Ingrese usuario: ")
    password = raw_input("Ingrese password: ")
    if login(usuario,password)==1:
        logon = True
    else:
        print("Error de login")

# Instanciar juego e iniciarlo
g = Game()
while True:
    g.new()
    g.run()
    if Partida.gano:
        g.show_ganaste()
    if Partida.perdio:
        g.show_perdiste()
    g.quit()
