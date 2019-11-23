from math import ceil

q = int(input())
for j in range(q):
    n, x = map(int, input().split())
    m = 0
    mm = 0
    for i in range(n):
        d, h = map(int, input().split())
        m = max(d, m)
        mm = max(mm, d - h)
    if mm <= 0 and m < x:
        print(-1)
    else:
        if m >= x:
            print(1)
        else:
            print(1 + ceil((x - m) / mm))
