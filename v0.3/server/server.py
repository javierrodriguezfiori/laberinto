import SocketServer
import threading
import time
from settings import *
import sys
import pickle
from os import path

def load_map(map_data):
    game_folder = path.dirname(__file__)
    with open(path.join(game_folder, 'map.txt'), 'rt') as f:
        for line in f:
            map_data.append(line)

class MiTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = self.request.recv(1024)
            if (data == "map"):
                print ("Request de mapa recibida de: "+str(self.client_address))
                mapa=pickle.dumps(map_data)
                self.request.send(mapa)
                print ("Mapa enviado a: "+str(self.client_address))
        except:
            print "Cliente desconectado"

class ThreadServer(SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def main():
    server = ThreadServer((host,port),MiTCPHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print "Server corriendo en: ", host, ":", port

map_data = []
load_map(map_data)
main()
