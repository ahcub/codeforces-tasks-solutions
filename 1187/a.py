t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    print(max((n - m), (n-k)) + 1)
