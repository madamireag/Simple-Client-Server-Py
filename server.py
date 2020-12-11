# server
import socket
import time


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

portTyped = input('Tell me the port: ')
host = socket.gethostname()
port = int(portTyped)

serversocket.bind((host, port))
print('Bind done')

serversocket.listen(1)
print('Listening')


clientsocket,addr = serversocket.accept()
print("Got connection from %s" % str(addr))
data = clientsocket.recv(1024).decode()
print('Received message from client: ')
print(data)
while data != 'exit':
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.sendall(currentTime.encode())
    data = clientsocket.recv(1024).decode()
    print('Received message from client:')
    print(data)
clientsocket.close()
serversocket.close()