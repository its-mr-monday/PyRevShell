#
#
#   PyRevShell Client Function Library v1.0
#
#

import platform
import getpass
import sys
from shell_class import *
from crypto_lib import *
from crypto_lib import Encryption as Crypto


def getuname():     #Returns the name of the currently signed in user
    return getpass.getuser()

def os_check():     #Check the systems operating systen
    plat = platform.system()
    if plat == "Darwin":
        plat = "MacOS"
    return plat

class Client:   #client class
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ostype = os_check()
        
def shell_test():
    sysos = os_check()
    shell = Shell(sysos)
    x = 0
    while x in range(0,1):
        
        cmd = input("> ")
        if cmd == "exit":
            shell.shell_close()
            sys.exit()
        elif ("cd ") in cmd:
            output = shell.shell_cd_handle(cmd)
        else:
            output = shell.shell_interact(cmd)
        print(output)
        
