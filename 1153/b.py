n, m, h = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    t = list(map(int, input().split()))
    print(' '.join(str(min(a[j], b[i]) if v != 0 else 0) for j, v in enumerate(t)))
