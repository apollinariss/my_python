import random
n = ['самовар','весна','лето']
s = random.choice(n)
lst = list(s)
p = random.choice(lst)
lst[p] = '?'
s = ''.join(lst)
print(s)
