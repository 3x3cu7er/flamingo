"""                  ##############################        
            ################################################
     ############            [UDP,TCP]               ##############
        ############   PROGRAMMING WITH SOCKETS  ##############
            ##############################################
                    ##############################

The code first accept authentications, if the credentials are valid, then
the process(code) continues. Otherwise the process(code) is stopped(quit).
The password is initialized using a dictionary, the default credentials are
            password_dict = {
    'root': {
        'admin': *********************,
        'annonymous':******************
    }

}
Afterwards the program continues normally.

NOTE : THIS IS FOR A SOCKETS TRIALS.

CODED_BY : ~JUPITER~,
PROGRAM_HEADER : NETWORK,
CODE_STATUS : NORMAL

~ SOCKETS ~

"""


import random
import socket
import logging
import sys

from colorama import Fore
import time

print(Fore.BLUE + __doc__)

sessions = int(input(Fore.GREEN + "Enter the number of sessions to be established $"))

auth = """
    ##########################################################################
    ##########   AUTHENTICATION(ROOT) NEEDED FOR THIS PROCESS   ##############
    ##########################################################################
"""
print(auth)

# <<<<<<<<<<<<<<password >>>>>>>>>>>>>>>>>>>>

password_dict = {
    'root': {
        'admin': ['cyber454', 'annonyms'],
        'annonymous':['bc101618@kaliadmin','bc101618@','bc101618']
    }

}

name = input("Login as [rootUser,OtherUser] $")
password = input(f"Enter password for {name} :hint\'cyber454\' $")

if name == 'root' and password in password_dict['root']['admin']:
    time.sleep(10)
    print(Fore.YELLOW + "~access granted~")
else:
    time.sleep(10)
    print(Fore.YELLOW + "~access denied~")
    sys.exit()

for session in range(sessions):
    print(f'SESSION {session + 1}'.center(50, '*'))
    permission = input('Do you want to continue: [yes(y)/no(n)] $')
    for stars in range(100):
        if stars == 0:
            print(f'Establishing session {session + 1}', end='')
        if stars == 99:
            if permission.lower() == 'yes' or permission.lower() == 'y':
                print(Fore.YELLOW + f'Permission granted @session{session + 1}')
                sys.getprofile()
            else:
                print(Fore.RED + f'~permission denied @session{session + 1}~\nSystem terminating..')
                time.sleep(5)
                sys.exit()
        print('.', end='')
        time.sleep(0.01)

    try:

        logger = logging.getLogger("Cyber$")

        server = random.randint(1000, 9999)

        print(Fore.YELLOW + """A program to listen/connect to the socket....""".center(40, '*'))

        host = str(input(Fore.GREEN + "Host address $"))
        port = int(input("Port number [ftp,http,https,ssh,telnet,RIP...etc] $"))


        # <<<<<<<<<<<<<<<<<<<<<< connection class >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        class connect:
            def tcp_connect_sender(self):
                global host, port
                # <<<<<<<<<<<<<<<<<<<<<<<,sending criterion >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                soc.bind((socket.gethostbyname(host), port))
                soc.listen()
                while True:
                    client, address = soc.accept()
                    msg = input("Accept connection request: [yes(y)/no(n)] $")
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
                _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                _socket.bind((host, port))
                _socket.listen()
                while True:
                    client, address = _socket.accept()
                    client.send("This one is based on UDP connection".encode('ascii'))
                    print(Fore.BLUE + f"UDP connection established..@{address}")
                    client.close()

            def udp_connect_receiver(self):
                _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                _socket.connect((host, port))
                msg = _socket.recv(1024).decode('ascii')
                print(Fore.GREEN + msg)
                _socket.shutdown(5)


        conn = connect()

        request = input("Sending (S) or Receiving(R) $")

        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< protocol selection >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

        try:
            protocol = str(input("Protocol to use [tcp,udp] $"))

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
                        #sys.exit(1)

                time.sleep(0.05)

            if protocol.upper() == 'TCP':
                print(Fore.BLUE + "TCP protocol selected !")
                print(Fore.YELLOW)
                if request.upper() == 'SENDING' or request.upper() == 'S':
                    time.sleep(5)
                    conn.tcp_connect_sender()

                elif request.upper() == 'RECEIVING' or request.upper() == 'R':
                    time.sleep(5)
                    conn.tcp_connect_receiver()

                else:
                    time.sleep(15)
                    invalid_input = "< Hello there, Please you must select a format >"
                    print(invalid_input.center(11, '#'))

            elif protocol.upper() == 'UDP':
                print(Fore.BLUE + "UDP protocol selected !")
                if request.upper() == 'SENDING' or request.upper() == 'S':
                    time.sleep(5)
                    conn.udp_connect_sender()
                elif request.upper() == 'RECEIVING' or request.upper() == 'R':
                    time.sleep(5)
                    conn.udp_connect_receiver()
                else:
                    time.sleep(15)
                    invalid_input = "< Hello there, Please you must select a format >"
                    print(invalid_input.center(11, '#'))
            else:
                print("No protocol selected.....please try again")


        except socket.error as err:
            err_message = "~Session closed unexpectedly ~"
            logger.warning(err_message)
            print(err)
    except Exception as ec:
        print(ec)

