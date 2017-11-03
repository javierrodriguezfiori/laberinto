import SocketServer
import threading
import time

class MiTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = ""
        while data != "salir":
            try:
                data = self.request.recv(1024)
                print data
                time.sleep(0.1)
            except:
                print "No se puede establecer conexion con el cliente"
                data = "salir"

class ThreadServer(SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def main():
    host = "localhost"
    port = 5000
    server = ThreadServer((host,port),MiTCPHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print "Server corriendo..."

main()
