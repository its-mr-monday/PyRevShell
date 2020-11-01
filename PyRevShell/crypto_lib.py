from Cryptodome.PublicKey import RSA
from Cryptodome import Random
import socket

class Encryption:   #Encryption class using RSA key pairs
    def __init__(self): #Initialise by generating 2 RSA keys
        random_generator = Random.new().read
        self.priv_key = RSA.generate(1024, random_generator)
        self.pub_key = priv_key.publickey()
    
    def recv_pubkey(self, socket):  #class handler function for receicing a pubkey over socket
        socket.send("public_key="+self.pub_key.exportKey()+"\n")
        print("Sent public RSA Key")
        
    def send_pubkey(self, socket):  #class handler function for sending a pubkey over socket
        pubkeystring = socket.recv(1024)
        pubkeystring = pubkeystring.replace("public_key=", '')
        pubkeystring = pubkeystring.replace("\r\n", '')
        self.sock_pub_key = RSA.importKey(pubkeystring)
        
    def encrypt_msg(self, msg):     #class handler function for encrypting msg with socket public key
        encrypted_msg = self.sock_pub_key.encrypt(msg, 32)
        return encrypted_msg
    
    def decrypt_msg(self, msg):     #class handler function for decrypting msg with RSA private key
        decrypted_msg = self.priv_key.decrypt(msg)
        return decrypted_msg