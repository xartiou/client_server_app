# Примеры слов и соответствующие наборы юникод-символов:
# "Компьютер", \u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440
# "Программа", \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430
# "Интернет", \u0418\u043d\u0442\u0435\u0440\u043d\u0435\u0442


# Комбинации параметров символов в системе Unicode:
# U+0061, "LATIN SMALL LETTER A" - a
# U+00E4, "LATIN SMALL LETTER A WITH DIAERESIS" - ä
# U+0056, "LATIN CAPITAL LETTER V" - V
# U+0026, "AMPERSAND" - &
# U+003B, "SEMICOLON" - ;

# --- Unicode в Python 3---

# progr_1 = 'Программирование'
# print(progr_1)
# Out: Программирование
#
# print(type(progr_1))
# Out: <class 'str'>
#
# progr_2 = 'Programování'
# print(progr_2)
# Out: Programování
#
# unic_s_1= "\N{LATIN SMALL LETTER C WITH DOT ABOVE}"
# print(unic_s_1)
# Out: ċ
# unic_s_2 = "\u010B"
# print(unic_s_2)
# Out: ċ

# progr_3 = 'Программа'
# progr_4 = '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
# print(progr_4)
# Out: Программа
# print(progr_3 == progr_4)
# Out: True
# print(len(progr_4))
# Out: 9
# print(ord('ã'))
# Out: 227
# print(chr(227))
# Out: ã

# ---Байты---

# bytes_s_1 = b'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'
# bytes_s_2 = b"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430"
# bytes_s_3 = b'''\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430'''
# print(type(bytes_s_1))
# Out: <class 'bytes'>

# In[21]: bytes_s_4 = b'Program'
# In[22]: print(bytes_s_4)
# Out[22]: b'Program'
# In[23]: print(len(bytes_s_4))
# Out[23]: 7


# Если указать в байтовом типе данных символ, не относящийся к ASCII, появится сообщение об
# ошибке
# bytes_s_5 = b'Программа'
# print(bytes_s_5)
# Out[25]:
# File "C:\Users\Администратор\Desktop\Курс Питон 2.1\01.
# Концепции хранения информации\examples\01_unicode_in_python3\
# bytes.py", line 15
# bytes_s_5 = b'Программа'
# ^
# SyntaxError: bytes can only contain ASCII literal characters.


# ---Конвертация байтов и строк---

# enc_str = 'Кодировка'
# enc_str_bytes = enc_str.encode('utf-8')
# print(enc_str_bytes)
# Out:b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0'


# dec_str_bytes = b'\xd0\x9a\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0'
# dec_str = dec_str_bytes.decode('utf-8')
# print(dec_str)
# Out: Кодировка

# str_1 = 'Программа'
# str_1_enc = str.encode(str_1, encoding='utf-8')
# print(str_1_enc)
# Out: b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0'

# bytes_1 = b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0'
# bytes_1_enc = bytes.decode(bytes_1, encoding='utf-8')
# print(bytes_1_enc)
# Out: Программа

# bytes_1 = b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb0'
# bytes_1_enc = bytes.decode(bytes_1, 'utf-8')
# print(bytes_1_enc)
# Out: Программа

# ---Примеры конвертации байтов и строк---

# import subprocess
# args = ['ping', 'google.com']
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in subproc_ping.stdout:
#     print(line)
# Out: b'\x8e\xa1\xac\xa5\xad \xaf\xa0\xaa\xa5\xe2\xa0\xac\xa8...'

# for line in subproc_ping.stdout:
#     print(line.decode('utf-8'))
# Out: UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8e in position 0: invalid start byte

# for line in subproc_ping.stdout:
#     line = line.decode('cp866').encode('utf-8')
# print(line.decode('utf-8'))
# Out: Обмен пакетами с google.com [74.125.232.224] с 32 байтами данных:
#     Ответ от 74.125.232.224: число байт=32 время=36мс TTL=56
#     Ответ от 74.125.232.224: число байт=32 время=36мс TTL=56
#     Ответ от 74.125.232.224: число байт=32 время=36мс TTL=56
#     Ответ от 74.125.232.224: число байт=32 время=36мс TTL=56
#     Статистика Ping для 74.125.232.224:
#     Пакетов: отправлено = 4, получено = 4, потеряно = 0 (0% потерь)
#     Приблизительное время приема-передачи в мс:
#         Минимальное = 36 мсек, Максимальное = 36 мсек, Среднее = 36 мсек

# ---Модуль telnetlib---
# import telnetlib
# import time
# tn_connect = telnetlib.Telnet('10.0.0.1')
# tn_connect.read_until(b'Username:')
# tn_connect.write(b'user\n')
# t.read_until(b'Password:')
# t.write(b'pass\n')
# time.sleep(5)
# output = tn_connect.read_very_eager().decode('cp866').encode('utf-8')
# print(output.decode('utf-8'))

#---Работа с файловой системой---

# with open(file_name) as f_n:
#     for el_str in f_n
#         print(el_str)

# import locale
# def_coding = locale.getpreferredencoding()
# print(def_coding)
# Out: cp1251

# f_n = open("test.txt", "w")
# f_n.write("test test test")
# f_n.close()
# print(f_n)
# Out: <_io.TextIOWrapper name='test.txt' mode='w' encoding='cp1251'>

# with open('test.txt', encoding='utf-8') as f_n:
# for el_str in f_n:
#     print(el_str, end='')
# Out: test test test

