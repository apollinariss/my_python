import random
x = int(input('Введите целое число\n'))
if random.randint(1,4) == x:
    print('Победа!')
elif random.randint(1,4) > x:
    print('Результат меньше введенного числа. Повторите еще раз!')
elif random.randint(1,4) < x:
    print('Результат больше введенного числа. Повторите еще раз!')
