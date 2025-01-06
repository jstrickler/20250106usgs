import socket
import os
from threading import Thread

def main():
    serv = setup()
    while True:
        (csock, addr) = serv.accept()
        t = Thread(target=handle_client, args=(csock,))
        t.start() # launch thread to handle client

def setup():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # serv.setblocking(0)

    serv.bind(('localhost', 7777))

    serv.listen(5)

    return serv


def handle_client(cli_sock):
    request = cli_sock.recv(1024)  # pid was 0, code is in child, handle client

    reply = request.upper()[::-1]  # upper & reversed

    cli_sock.sendall(reply)
    cli_sock.close()


if __name__ == '__main__':
    main()
