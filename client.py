import socket
import time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = s.connect(("pi", 5000))

def magnetic():
            data = s.recv(1024).decode("utf-8")
            return data

# while True:
#     print(magnetic())
#     time.sleep(1)