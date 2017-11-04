import SocketServer
import threading
import time
from settings import *
import sys
import pickle

class MiTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = ""
        while data != "salir":
            try:
                while 1:
                    data = self.request.recv(1024)
                    if not data: break
                    if (data == "map"):
                        print ("Request de Mapa recibida")
                        lista=[1,2,3,4]
                        mapa=pickle.dumps(lista)
                        print (lista)
                        print (mapa)
                        self.request.sendall(mapa)
            except:
                print "No se puede establecer conexion con el cliente"
                data = "salir"

class ThreadServer(SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def main():
    server = ThreadServer((host,port),MiTCPHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print "Server corriendo en: ", host, "-", port

main()
