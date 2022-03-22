"""Program time server"""

from socket import socket, AF_INET, SOCK_STREAM
import time

SERV_SOCK = socket(AF_INET, SOCK_STREAM)
SERV_SOCK.bind(('', 8800))    # привязываем подключение от клиентов
SERV_SOCK.listen()   # сигнал готовности

try:
    while True:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()   # принимаем запрос на подключение
        print(f"Получаем запрос на соединение от клиента с адресом и портом: {ADDR}")
        TIMESTR = time.ctime(time.time()) + "\n"   # формируем временнУю метку
        CLIENT_SOCK.send(TIMESTR.encode('utf-8'))   # превращаем метку в байты и отправляем клиенту
        CLIENT_SOCK.close()
finally:
    SERV_SOCK.close()
