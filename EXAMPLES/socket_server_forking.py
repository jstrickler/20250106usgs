import socket
import os


def setup():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # serv.setblocking(0)

    serv.bind(('localhost', 7777))

    serv.listen(5)

    return serv


def main():
    serv = setup()
    while True:
        (csock, addr) = serv.accept()
        handle_client(csock)


def handle_client(cli_sock):
    pid = os.fork()  # fork a new process; pid set to actual PID in parent, set to 0 in child
    if pid:  # if pid is non-0, then in parent, don't do anything else
        return
    request = cli_sock.recv(1024)  # pid was 0, code is in child, handle client

    reply = request.upper()[::-1]  # upper & reversed

    cli_sock.sendall(reply)
    cli_sock.close()


if __name__ == '__main__':
    main()
