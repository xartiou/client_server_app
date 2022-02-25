# 6. Создать текстовый файл test_file.txt,
# заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
# что перед нами файл в неизвестной кодировке.
# Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.

import locale
import chardet

print(locale.getpreferredencoding())
# cp1251
with open('test_file.txt', 'rb') as fl:
    s = fl.read()
    print(s)
    print(chardet.detect(s))
# b'\xd1\x81\xd0\xb5\xd1\x82\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb5
# \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\r\n\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82\r\n\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

with open('test_file.txt', encoding='utf-8', errors='replace') as fl:
    print(fl.read())
