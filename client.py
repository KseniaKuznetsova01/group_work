import socket
from concurrent.futures import ThreadPoolExecutor

def pp(sms):
    with socket.create_connection(('127.0.0.1', 10001)) as sock:
        sock.sendall(sms.encode('utf-8'))

with ThreadPoolExecutor(max_workers=4) as pool:
    for _ in range(100):
        pool.submit(pp)