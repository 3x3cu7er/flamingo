# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< A code for testing the connection >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import socket
from colorama import Fore

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(Fore.YELLOW + """A program to test the connect....""".center(40, '*'))

host = str(input(Fore.GREEN + "Host address $"))
port = int(input("Port number $"))


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<sending trials >>>>>>>>>>>>>>>>>>>>>>
def reply():
    soc.bind((host, port))
    soc.listen()
    while True:
        client, address = soc.accept()
        reply = input("Enter message : ")
        client.send(reply.encode('ascii'))
        print(f'Connected to {address}')
        return reply

rep = input("reply")

# <<<<<<<<<<<<<<<<<<<<<<<<receiving trials>>>>>>>>>>>>>>>>>>>>>>>
if rep=="reply ->":
    reply()
else:
    while True:
        soc.connect((host, port))
        print(soc.recv(1024).decode('ascii'))


