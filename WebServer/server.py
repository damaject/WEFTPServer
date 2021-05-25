# Created by Maxim on 25.05.2021 14:02

import os
import datetime
import socket as sc
import threading as th


def input_port():
    global DEFAULT_PORT
    while True:
        new_port = input(f'Press «Enter» to start web server on port {DEFAULT_PORT} or pre-input other port (1024-65535)\n> ')
        if new_port == '':
            return DEFAULT_PORT
        else:
            if new_port.isnumeric():
                new_port = int(new_port)
                if 1024 <= new_port <= 65535:
                    return new_port


def server_start(server, port):
    print(f'Starting web server on port {port}...')
    try:
        server.settimeout(1)
        server.bind(('', port))
        server.listen(100)
    except OSError:
        print(f'! Error starting web server on port {port}, try another port')
        return False
    print(f'Web server started on port {port}')
    return True


def server_listening(server):
    while True:
        try:
            new_conn, new_addr = server.accept()
            th.Thread(target=client_receiver, args=(new_conn, new_addr)).start()
        except sc.timeout:
            pass


def client_receiver(conn, addr):
    client = f'Client{addr[1]}'
    data = conn.recv(8192)
    data = data.decode()
    request_url = get_request_path(data)
    t = datetime.datetime.now().strftime("%H:%M:%S")
    print(f'{t} {client} [{addr[0]}:{addr[1]}] connected to web server to url: {request_url}')
    conn.send(get_page_content(request_url).encode())
    conn.close()


def get_request_path(resp_data):
    arr_data = resp_data.split(' ')
    return arr_data[1] if len(arr_data) > 0 else ''


def get_page_content(path):
    if path == '/':
        path = 'index.html'
    path = 'html/' + path
    path = path.replace('//', '/')
    header = 'HTTP/1.1 200 OK\r\nContent - Type: text / html;charset=utf-8\r\n\r\n'

    if not os.path.exists(path) or not os.path.isfile(path):
        path = 'html/404.html'
        header = 'HTTP/1.1 404 OK\r\nContent - Type: text / html;charset=utf-8\r\n\r\n'

    file = open(path, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return header + content


print('LdWebServer is started...')

DEFAULT_PORT = 80

socket = sc.socket()

while True:
    PORT = input_port()
    if server_start(socket, PORT):
        break
    if PORT == DEFAULT_PORT:
        DEFAULT_PORT = DEFAULT_PORT + 1

server_listening(socket)

print('LdWebServer is shutdown...')
