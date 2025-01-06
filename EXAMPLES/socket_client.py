import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a new TCP/IP socket

s.connect(('localhost', 7777))  # connect to server via (host, port) tuple

if len(sys.argv) > 1:
    msg = sys.argv[1]
else:
    msg = "default message"

s.sendall(msg.encode())  # send message (must be bytes, not str)

raw_reply = s.recv(4096)  # receive reply (as bytes) from server

# decode message from bytes to str 
# and strip any trailing whitespace
reply = raw_reply.strip().decode()

print(f"Server said >{reply}<")  

s.close()  # close connection
