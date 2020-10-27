
#IMPORT LIBRARY
import server_lib as lib
from GLOBAL import *
from _crypto import _crypto as Crypto

def main():
    s = lib.Server(SERV_HOST, ST_PORT, Crypto())
    socket_loop = 0
    while (socket_loop < 1):
        print("Awaiting connection . . .")
        s.socket_accept()
        s.closeSocket()
        socket_loop +=1
    return

main()