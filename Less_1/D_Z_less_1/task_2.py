# 2. Каждое из слов «class», «function», «method» записать в байтовом типе.
# Сделать это необходимо в автоматическом, а не ручном режиме,
# с помощью добавления литеры b к текстовому значению,
# (т.е. ни в коем случае не используя методы encode, decode или функцию bytes)
# и определить тип, содержимое и длину соответствующих переменных.

# вариант с конкатинацией
# word_1 = 'b' + "'class'"
# word_2 = 'b' + "'function'"
# word_3 = 'b' + "'method'"
#
# words = []
# words.append(eval(word_1))
# words.append(eval(word_2))
# words.append(eval(word_3))
#
# for word in words:
#     print(word,type(word),len(word))

# вариант с f string

word_1 = 'class'
word_2 = 'function'
word_3 = 'method'

words = [word_1, word_2, word_3]

for word in words:
    w = eval(f"b'{word}'")
    print('-' * 50)
    print('type: ', type(w))
    print(w)
    print('length of variable in bites: ', len(w))

