import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipadrr = "192.168.0.69"
s.bind((ipadrr, 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()

    print(f"Established connection with{address}")
    clientsocket.send(bytes("welcome to the server", "utf-8"))
