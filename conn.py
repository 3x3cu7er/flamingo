import os
interfaces = []


try:

    _cards = int(input("Number of interface cards : "))
    network_card = input("Network card : ")

except ValueError as nerr:
    print(nerr)

try:
    for card in range(_cards):
        interface = input(f"Interface card {card+1} name :")
        interfaces.append(interface)

    for  net in interfaces:
        if "eth" in net:
            try:
                ip = input(f"IP address for interface {net} : ")
                scan = os.system(f"nmap -Pn -sV {ip}")
            except OSError as err:
                raise OSError
    print(scan)
except Exception as exc:
    print(exc)

