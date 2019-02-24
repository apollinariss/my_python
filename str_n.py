def func(s,n):
    if len(s) > n:
        return(s.upper())
    else:
        return s

s = str(input('Введите строку\n'))
n = int(input('Введите целочисленное значение\n'))

print(func(s,n))
