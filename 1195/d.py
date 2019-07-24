from itertools import chain

n = int(input())
a = input().split()
ans = 0
def f(a):
    return int(''.join(chain(*zip(a,a))))*len(a)
for i in range(n):
    ans += f(a[i])
print(ans % 998244353)
