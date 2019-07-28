q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    if n == 1:
        t = int(input())
        if t % 2 == 1:
            print('YES')
            print(1)
        else:
            print('NO')
    else:
        a = list(map(int, input().split()))
        ans = []
        s = 0
        for j in range(n):
            s += a[j]
            if s % 2 and k > 1:
                ans.append(j+1)
                k -= 1
                s = 0
        if s % 2 and k == 1:
            print('YES')
            print(*ans, n)
        else:
            print('NO')
