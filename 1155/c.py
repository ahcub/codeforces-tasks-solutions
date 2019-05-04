from functools import reduce

from math import gcd

n, m = map(int, input().split())
x = list(map(int, input().split()))
p = list(map(int, input().split()))

x_0 = x[0]
x = [el - x_0 for el in x[1:]]
x_gcd = reduce(gcd, x)

for j, p_j in enumerate(p, 1):
    if x_gcd == p_j or (x_gcd > p_j and x_gcd % p_j == 0):
        print('YES')
        print(x_0, j)
        exit()
print('NO')
