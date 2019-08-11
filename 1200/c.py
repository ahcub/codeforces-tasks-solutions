from math import gcd

n, m, q = map(int, input().split())

w = gcd(n, m)
np = n // w
mp = m // w
for _ in range(q):
    sx, sy, ex, ey = map(int, input().split())
    sp = (sy-1) // (np if sx == 1 else mp)
    ep = (ey-1) // (np if ex == 1 else mp)
    if sp == ep:
        print('yes')
    else:
        print('no')
