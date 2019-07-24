from operator import itemgetter

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == n:
    print(0)
elif k == 1:
    print(a[-1] - a[0])
else:
    jumps = [0]*n
    jumps[0] = (0, 0)
    for i in range(1, n):
        jumps[i] = (a[i]-a[i-1], i)
    j = sorted(jumps, key=itemgetter(0))
    jj = sorted(j[-k+1:], key=itemgetter(1))
    ans = 0
    s = 0
    for _, i in jj:
        ans += a[i-1] - a[s]
        s = i
    ans += a[-1] - a[s]
    print(ans)
