q = int(input())
for _ in range(q):
    a = int(input())
    b = input()
    cc = b.count('1')
    if cc == 0:
        print(a)
    else:
        l = b.index('1')
        r = b.rindex('1')
        print((2 * (a - min(l, (a-1-r)))))
