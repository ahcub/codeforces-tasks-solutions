from math import floor

n = int(input())
s = 0

class Pair():
    def __init__(self, a, b):
        self.a = a
        self.b = b

numbers = []
for i in range(n):
    a = input()
    b = floor(float(a))
    numbers.append(Pair(b, a[-5:] != '00000'))
    s += b

i = 0
while s != 0:
    if numbers[i].b:
        numbers[i].a += 1
        s += 1
    i += 1
print(*(str(el.a) for el in numbers), sep='\n')
