
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.0.69", 1234))

while True:
    s.send(bytes("prepare", "utf-8"))
    msg = s.recv(1024)
    if "send" == msg.decode("utf-8"):
        print(msg.decode("utf-8"))




