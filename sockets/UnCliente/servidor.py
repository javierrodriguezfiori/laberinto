import SocketServer

class MiTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        self.num = len(self.data)
        print "La data recibida es ", self.data
        self.request.send(str(self.num))

def main():
    host = "localhost"
    port = 5000

    server1 = SocketServer.TCPServer((host,port),MiTCPHandler)
    print "Server UP"
    server1.serve_forever()

main()
