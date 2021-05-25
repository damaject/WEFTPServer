# Created by Maxim on 05.04.2021 0:17

import socket as sc


def input_port():
    global DEFAULT_PORT
    while True:
        new_port = input(f'Press «Enter» to start client on server port {DEFAULT_PORT} or pre-input other port (1024-65535)\n> ')
        if new_port == '':
            return DEFAULT_PORT
        else:
            if new_port.isnumeric():
                new_port = int(new_port)
                if 1024 <= new_port <= 65535:
                    return new_port


def client_start(client, port):
    print(f'Starting client on server port {port}...')
    try:
        client.connect(('localhost', port))
    except OSError:
        print(f'! Error connect to server on port {port}, try another port')
        return False
    print(f'Client connected to server on port {port}')
    return True


print('LdEchoClient is started...')

DEFAULT_PORT = 20000
socket = sc.socket()

while True:
    PORT = input_port()
    if client_start(socket, PORT):
        break
    if PORT == DEFAULT_PORT:
        DEFAULT_PORT = DEFAULT_PORT + 1


while True:
    data = input('> ')
    if data == 'exit':
        print(f'Client disconnected from server')
        break
    try:
        print(f'Client send data to server: «{data}»')
        socket.send(data.encode())
        data = socket.recv(1024)
        data = data.decode()
        print(f'Client receive data from server: «{data}»')
    except OSError:
        print(f'! Error send data, server disconnect')
        break

socket.close()

print('LdEchoClient is finished...')
