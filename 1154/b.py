n = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))
if len(b) > 3:
    print(-1)
elif len(b) == 3:
    low, mid, high = b
    if mid - low != high - mid:
        print(-1)
    else:
        print(mid - low)
elif len(b) == 2:
    s = sum(b)
    if (s % 2) != 0:
        print(b[1] - b[0])
    else:
        print(s // 2 - b[0])
else:
    print(0)