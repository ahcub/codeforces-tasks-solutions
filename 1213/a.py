n = int(input())
a = list(map(int, input().split()))
ans = 100
for i in a:
    s = 0
    for j in a:
        s += abs(i - j) % 2
    ans = min(ans, s)
print(ans)
