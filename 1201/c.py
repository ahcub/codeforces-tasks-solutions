n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
m = n // 2

p = a[m]
t = k
c = 1
for i in range(m+1, n):
    d = a[i] - p
    r = t - (c * d)
    if r == 0:
        print(a[i])
        exit()
    elif r < 0:
        print(a[i-1] + t // c)
        exit()
    else:
        c += 1
        p = a[i]
        t = r
print(a[n-1] + t // c)
