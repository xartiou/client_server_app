# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.
import platform
import subprocess

import chardet
from chardet import detect

urls = ['yandex.ru', 'youtube.com']

# --- вариант 1 ---
# пингование для windows
if platform.system().lower() == 'windows':
    code = '-n'
else:
    code = '-c'

for url in urls:
    args = ['ping', code, '4', url]
    YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        result = detect(line)
        print(result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

# --- вариант 2 ---
# for url in urls:
#     ping_ya = subprocess.Popen(('ping', url), stdout=subprocess.PIPE)
#
#     for i, line in enumerate(ping_ya.stdout):
#         result = chardet.detect(line)
#         line = line.decode(result['encoding']).encode('utf-8')
#         if i < 5:
#             print(line.decode('utf-8'))
#         else:
#             ping_ya.kill()

#  --- вариант 3 ---
# def ping_service(service):
#     args = ['ping', service]
#     ping = subprocess.Popen(args, stdout=subprocess.PIPE)
#     count = 0  #  для прерывания пингования
#     for line in ping.stdout:
#         result = chardet.detect(line)
#         line = line.decode(result['encoding']).encode('utf-8')
#         print(line.decode('utf-8'))
#         if count == 4:
#             break
#         count += 1
#
# ping_service('yandex.ru')
# ping_service('youtube.com')
