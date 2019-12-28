q = int(input())

for _ in range(q):
    n, x, a, b = map(int, input().split())
    print(min(abs(a-b) + x, n-1))
