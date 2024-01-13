import random
import socket
import logging
import sys

from colorama import Fore
import time

logger = logging.getLogger("Cyber$")

server = random.randint(1000,9999)

print(Fore.YELLOW + """A program to listen the connect....""".center(40, '*'))

host = str(input(Fore.GREEN + "Host address $"))
port = int(input("Port number $"))


# <<<<<<<<<<<<<<<<<<<<<< connection class >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class connect:
    def tcp_connect_sender(self):
        global host, port
        # <<<<<<<<<<<<<<<<<<<<<<<,sending criterion >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        soc.bind((host, port))
        soc.listen()
        while True:
            client, address = soc.accept()
            msg = input("Accept connection request: yes(y)/no(n) $")
            if msg.lower() == 'yes' or msg.lower() == 'y':
                client.send(f"Connection accepted @server {server}".encode('ascii'))
                print(f"Connection made with the host @{address}")
            else:
                sys.exit()

    def tcp_connect_receiver(self):
        global host, port
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<receiving criterion >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((host, port))
        message = soc.recv(1024).decode('ascii')
        print(message)

    def udp_connect_sender(self):
        pass

    def udp_connect_receiver(self):
        pass


conn = connect()

request = input("Sending (S) or Receiving(R) $")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< protocol selection >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

try:
    protocol = str(input("Protocol in use $"))

    time.sleep(5)

    for index in range(0, 50):
        if index == 0:
            print(Fore.BLUE + "Checking for protocol status", end='')
        print('.', end='')
        if index == 49:
            _exist = {
                'tcp': 'TCP',
                'udp': 'UDP'
            }
            if protocol in _exist:
                print('OK\n')
            else:
                print('Invalid!')

        time.sleep(0.05)

    if protocol.upper() == 'TCP':
        print(Fore.BLUE + "TCP protocol selected !")
        print(Fore.YELLOW)
        if request.upper() == 'SENDING' or request.upper() == 'S':
            time.sleep(5)
            conn.tcp_connect_sender()

        elif request.upper() == 'RECEIVING' or request.upper() == 'R':
            conn.tcp_connect_receiver()

        else:
            time.sleep(15)
            invalid_input = "< Hello there, Please you must select a format >"
            print(invalid_input.center(11, '#'))

    elif protocol.upper() == 'UDP':
        print(Fore.BLUE + "UDP protocol selected !")
    else:
        print("No protocol selected.....please try again")


except:
    err_message = "~Session closed unexpectedly ~"
    logger.warning(err_message)
