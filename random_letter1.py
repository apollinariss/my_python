import random
n = ['самовар','весна','лето']
random_word = random.choice(n)
lst = list(random_word)
random_letter = random.choice(lst)
index_lst = lst.index(random_letter)
lst[index_lst] = '?'
s = ''.join(lst)
print(s)
guess = str(input('Введите букву: \n'))
if guess == random_letter:
    print('Победа! Загаданное слово - ', random_word)
else:
    print('Увы! Попробуйте в другой раз. Загаданное слово - ', random_word)
