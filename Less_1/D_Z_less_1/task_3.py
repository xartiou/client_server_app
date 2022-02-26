# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

words = ['attribute','класс','функция', 'type']

# вариант с длиной слова
# for w in words:
#     if len(w.encode('ascii', 'ignore')) == len(w):
#         print('OK')
#     else:
#         print('невозможно записать в байтовом типе')

# --- bytes и UnicodeEncodeError ---
# for w in words:
#     try:
#         bytes(w, 'asii')
#     except UnicodeEncodeError:
#         print(f'Слово "{w}" невозможно записать в виде байтовой строки')

# --- encode и UnicodeEncodeError ---
# for w in words:
#     try:
#         w.encode('ascii')
#     except UnicodeEncodeError:
#         print(f'Слово "{w}" невозможно записать в виде байтовой строки')

# eval и SyntaxError
# for w in words:
#     try:
#         new_w = f"b'w'"
#         eval(new_w)
#     except SyntaxError:
#         print(f'Слово "{w}" невозможно записать в виде байтовой строки')

# проверка через ORD
# for w in words:
#     for l in w:
#         if ord(l) > 127:
#             print(f'Слово "{w}" невозможно записать в виде байтовой строки')
#             break

# если не ascii
for w in words:
    if not w.isascii():
        print(f'Слово "{w}" невозможно записать в виде байтовой строки')