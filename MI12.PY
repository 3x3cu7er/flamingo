import time
import threading
import socket
import concurrent.futures
import os 
import sys
import subprocess
from colorama import Fore


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 22

listener = sock.bind((host, port))
sock.listen()
print( f"{Fore.GREEN}Server~> in {Fore.RED}listening mode.")
while True:
    client, address = sock.accept()
    print(f'New agent Activated ->{address}'.encode('ascii'))
    time.sleep(2)
    client.send("Connected..".encode('ascii'))
    print('waiting for user handle ..')
msg = sock.recv(1024)
print(msg.decode('ascii'))


