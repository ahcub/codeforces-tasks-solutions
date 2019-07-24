n = int(input())
for i in range(n):
    m = int(input())
    a = sorted(list(map(int, input().split())))
    if len(a) > 2:
        b, d = a[-2:]
        min1 = min(b, d)
        if min1 >=2:
            print(min(len(a)-2, min1-1))
            continue
    print(0)
