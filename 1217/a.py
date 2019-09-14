q = int(input())
for j in range(q):
    s, i, e = map(int, input().split())
    if s + e > i:
        print(min((e + 1 + (s - i)) // 2, e + 1))
    else:
        print(0)
