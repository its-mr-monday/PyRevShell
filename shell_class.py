import os
import subprocess

win_drives = ["C:","D:","E:","F:"]

def find_powershell():
    drive_index = r"\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    for x in range(0,len(win_drives)):
        base_str = win_drives[x]+drive_index
        print(base_str)
        if os.path.isfile(base_str):
            print(base_str)
            x = len(win_drives)
            return base_str
        else:
            x+=1

class Shell:
    def __init__(self, sys_type):   #Initialization of the shell class finds the location of a terminal and opens a shell
        self.terminal = ""
        if sys_type == "Windows":
            self.terminal +=find_powershell()
        else:
            self.temrinal = '/bin/bash'
        self.open_shell()
            
    def open_shell(self):     #handle for opening a shell after a command has been parsed
        self.shell = subprocess.Popen([self.terminal], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
    def shell_output(self):
        output = ""
        for line in iter(self.shell.stdout.readline, b''):
            output += line.decode('utf-8')
        return output
    
    def shell_interact(self, cmd):  #interact with the current shell before opening a new one
        output = self.shell.communicate((cmd+"\n").encode())[0].decode()
        self.shell_close()
        self.open_shell()
        return output
    
    def shell_close(self):      #close the currently active shell
        self.shell.terminate()
        return 0

    def shell_cd_handle(self, cmd): #if command is cd make python change the directory
        self.shell_close()
        dir = cmd[3:len(cmd)]

        check = os.path.isdir(dir)
        if check == True:
            os.chdir(dir)
            return "Changed to dir "+dir
        else:
            return "Error invalid dir "+dir