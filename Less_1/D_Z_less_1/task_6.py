# 6. Создать текстовый файл test_file.txt,
# заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
# что перед нами файл в неизвестной кодировке.
# Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.

from chardet import detect

# записываем в файл
lines_lst = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    for line in lines_lst:
        file.write(f'{line}\n')
file.close()

# узнаем кодировку
with open('test_file.txt', 'rb') as file:
    content = file.read()
encoding = detect(content)['encoding']
print(encoding)

# открываем файл в правильной кодировке
with open('test_file.txt', 'r', encoding=encoding) as file:
    content = file.read()
print(content)