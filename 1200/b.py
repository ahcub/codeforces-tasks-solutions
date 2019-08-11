t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 'yes'
    for i in range(n-1):
        diff = h[i] - h[i+1] + k
        t = diff - max(diff - h[i], 0)
        if (diff + m) >= 0:
            m += t
            h[i] -= t
        else:
            ans = 'no'
            break
    print(ans)
