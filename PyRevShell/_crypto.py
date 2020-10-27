#CRYPTO MODULE FOR PYREVSHELL

import rsa
import socket
import pickle

class _crypto:

    def __init__(self):
        _pubKey, _privKey = rsa.newkeys(1024)
        self.publicKey = _pubKey
        self.privateKey = _privateKey

    def getEndpointPubKey(self, socket):
        endpublicKey = socket.recv(1024)
        self.endpointPubKey = pickle.loads(endpublickey)
        return

    def sendEndpointPubKey(self, socket):
        socket.send(pickle.dumps(self.publicKey))
        return

    def Encrypt(self, message):
        encrypted_msg = rsa.encrypt(message, self.endpointPubKey)
        return encrypted_msg

    def Decrypt(self, message):
        decrypted_msg = rsa.decrypt(message, self.privateKey)
        return decrypted_msg