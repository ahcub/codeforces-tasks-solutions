from math import ceil

q = int(input())
for i in range(q):
    a,b,c,d,k = map(int, input().split())
    p = ceil(a / c)
    pp = ceil(b/d)
    if p + pp > k:
        print(-1)
    else:
        print(p, pp)
