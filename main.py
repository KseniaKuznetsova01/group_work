import socket
import threading



def proc_request(conn, addr):
    print('Klient :', addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))

with socket.socket() as sock:
    sock.bind(('127.0.0.1',10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        th = threading.Thread(target = proc_request, args = (conn, addr))
        th.start()