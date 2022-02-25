# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

words = ['attribute','класс','функция', 'type']

for w in words:
    if len(w.encode('ascii', 'ignore')) == len(w):
        print('OK')
    else:
        print('невозможно записать в байтовом типе')

