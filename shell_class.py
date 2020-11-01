#
#
#   pyInteractive system shell class module v1.3
#   Developed by its-mr-monday and CyberM 2020
#   
#

import os
import subprocess

class Shell:    #Interactive shell class
    def __init__(self, sys_type):   #Initialization of the shell class finds the location of a terminal and opens a shell
        self.terminal = ""
        if sys_type == "Windows":
            self.find_powershell(["C:","D:","E:","F:"])
            self.terminal = self.powershell
        else:
            self.temrinal = '/bin/bash'
        self.open_shell()
            
    def open_shell(self):     #handle for opening a shell after a command has been parsed
        self.shell = subprocess.Popen([self.terminal], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def shell_interact(self, cmd):  #interact with the current shell before opening a new one
        output = self.shell.communicate((cmd+"\n").encode())[0].decode()
        self.shell_close();self.open_shell()
        return output
    
    def shell_close(self):      #close the currently active shell
        self.shell.terminate()
        return 0

    def find_powershell(self, win_drives):  #used to find powershell in order to start it
        drive_index = r"\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
        for x in range(0,len(win_drives)):
            base_str = win_drives[x]+drive_index
            print(base_str)
            if os.path.isfile(base_str):
                print(base_str)
                x = len(win_drives)
                self.powershell = base_str
            else:
                x+=1
                
    def shell_cd_handle(self, cmd): #if command is cd make python change the directory
        self.shell_close()
        dir = cmd[3:len(cmd)]

        check = os.path.isdir(dir)
        if check == True:
            os.chdir(dir)
            return "Changed to dir "+dir
        else:
            return "Error invalid dir "+dir