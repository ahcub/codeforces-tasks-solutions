t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    min = a[-1]
    for i in range(n-1, -1, -1):
        if a[i] > min:
            ans += 1
        else:
            min = a[i]
    print(ans)
