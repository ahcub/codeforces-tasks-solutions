a,b = input(), input()

ans = t = 0
for i in range(len(b)):
    t += a[i] != b[i]
ans += t%2==0
for i in range(len(b), len(a)):
    t += a[i] != a[i - len(b)]
    ans += t%2==0
print(ans)
