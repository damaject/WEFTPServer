# Created by Maxim on 05.04.2021 0:17

import socket as sc
import threading as th


def input_port():
    global DEFAULT_PORT
    while True:
        new_port = input(f'Press «Enter» to start server on port {DEFAULT_PORT} or pre-input other port (1024-65535)\n> ')
        if new_port == '':
            return DEFAULT_PORT
        else:
            if new_port.isnumeric():
                new_port = int(new_port)
                if 1024 <= new_port <= 65535:
                    return new_port


def client_receiver(conn, addr):
    global client_count, client_shutdown, client_shutdown_log
    client = f'Client{addr[1]}'
    print(f'{client} [{addr[0]}:{addr[1]}] connected to server')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode()
        print(f'Server receive data from {client}: «{data}»')
        if data == 'stop_server':
            client_shutdown = True
            client_shutdown_log = f'{client} shutdown server'
            data = 'You shutdown server!'
        print(f'Server send data to {client}: «{data}»')
        conn.send(data.encode())
        if client_shutdown:
            break
    conn.close()
    client_count -= 1
    print(f'{client} disconnected from server')


def server_start(server, port):
    print(f'Starting server on port {port}...')
    try:
        server.settimeout(1)
        server.bind(('', port))
        server.listen(100)
    except OSError:
        print(f'! Error starting server on port {port}, try another port')
        return False
    print(f'Server started on port {port}')
    return True


def server_listening(server):
    global client_count, server_shutdown
    while True:
        try:
            new_conn, new_addr = server.accept()
            th.Thread(target=client_receiver, args=(new_conn, new_addr)).start()
            client_count += 1
            server_shutdown = 30
        except sc.timeout:
            pass

        if client_count == 0:
            server_shutdown -= 1
            if 0 < server_shutdown <= 5:
                print(f'Server shutdown after {server_shutdown} seconds...')
            if server_shutdown <= 0:
                break

        if client_shutdown:
            print(client_shutdown_log)
            break


print('LdEchoServer is started...')

DEFAULT_PORT = 20000
client_count = 0
client_shutdown = False
client_shutdown_log = ''
server_shutdown = 0
socket = sc.socket()

while True:
    PORT = input_port()
    if server_start(socket, PORT):
        server_shutdown = 30
        break
    if PORT == DEFAULT_PORT:
        DEFAULT_PORT = DEFAULT_PORT + 1

server_listening(socket)

print('LdEchoServer is shutdown...')
