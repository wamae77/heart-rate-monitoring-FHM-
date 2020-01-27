
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipadrr = "192.168.0.69"
s.bind((ipadrr, 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    addr = socket.gethostbyaddr(address[0])

    print(f"Established connection with{address}")

    clientsocket.send(bytes(f"welcome to the server{addr}", "utf-8"))

    mag = clientsocket.recv(1234)
    print(mag.decode("utf-8"))
    if "prepare" == mag.decode("utf-8"):
        clientsocket.send(bytes("send", "utf-8"))
