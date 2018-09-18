"""http://codeforces.com/problemset/problem/1041/B"""

from math import gcd

a, b, x, y = map(int, input().split())
d = gcd(x, y)
x //= d
y //= d
print(min(a // x, b // y))