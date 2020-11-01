from crypto_lib import *
from crypto_lib import Encryption as Crypto

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        