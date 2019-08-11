n, m = map(int, input().split())

reg = [[0]*5 for i in range(m)]
g = ord('A')
for i in range(n):
    a = input()
    for j in range(m):
        reg[j][ord(a[j]) - g] += 1

ans = 0
vals = list(map(int, input().split()))
for i in range(m):
    ans += vals[i] * max(reg[i])
print(ans)
