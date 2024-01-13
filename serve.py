import socket

socStream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socStream.bind(("localhost", 6055))

while True:

    socStream.listen(6)

    client,addr = socStream.accept()

    index = 0
    index+=1

    client.send(f"{index} message  recieved".encode('utf-8'))


    print(f"Sent message {index}".encode('utf-8'))

  

