# client.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

portTyped = input('Tell me the port: ')
host = socket.gethostname()
port = int(portTyped)

s.connect((host, port))
print('Connected to server')

data = input('Type a message: ')
while data != 'exit':
    s.sendall(data.encode())
    message = s.recv(1024).decode()
    print('Message sent by server at: %s' % message)
    data = input('Type a message: ')

s.send(data.encode())
print('Connection closed')