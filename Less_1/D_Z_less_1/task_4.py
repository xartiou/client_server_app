# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode)

words = ['разработка', 'администрирование', 'protocol', 'standard']
words_enc = []
print('Байтовое преобразование.')
print()
for w in words:
    w_enc = w.encode('utf-8')
    words_enc.append(w_enc)
    print(w_enc)
print()
print('Обратное преобразование')
print()
for w_enc in words_enc:
    w_dec = w_enc.decode('utf-8')
    print(w_dec)

