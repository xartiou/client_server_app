"""Program client time"""

from socket import socket, AF_INET, SOCK_STREAM

CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)   # создаём сокет
CLIENT_SOCK.connect(('localhost', 8800))  # подключаемся к серверу
TIME_BYTES = CLIENT_SOCK.recv(1024)  # ждём ответа от сервера
print(f"Текущее время {TIME_BYTES.decode('utf-8')}")
CLIENT_SOCK.close()
