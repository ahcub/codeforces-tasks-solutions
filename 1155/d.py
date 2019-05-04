n, x = map(int, input().split())
a = list(map(int, input().split()))
inf = - 2**64
dp = [[[inf for _ in range(3)] for _ in range(3)] for _ in range(n+1)]

dp[0][0][0] = 0
for i in range(n+1):
    for j in range(3):
        for k in range(3):
            if k < 2:
                dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k])
            if j < 2:
                dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k])
            if i < n:
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k] + (a[i] if j == 1 else 0) * int(x if k == 1 else 1))
print(dp[n][2][2])