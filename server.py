import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket succesfuly created')
serv.bind(('localhost', 12345))
print('socket bound')
serv.listen(5)
while True:
    conn, addr = serv.accept()
    print('Got connection from', addr)
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data:
            break

        file = open("rawData", "wb")
        file.write(data)
        file.close()
        data_rev = data[::-1]

        # send back reversed data to client
        conn.send(data_rev)
        conn.close()
        print('client disconnected')





