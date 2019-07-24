q = int(input())
for i in range(q):
    n, m = map(int, input().split())
    rows_map = [[0 for _ in range(m)] for _ in range(n)]
    cols = [m]*m
    rows = [n]*n
    for j in range(n):
        for i, c in enumerate(input()):
            if c == '*':
                cols[i] -= 1
                rows[j] -= 1
            else:
                rows_map[j][i] = -1
    ans = n+m
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            ans=min(ans, r+c+rows_map[i][j])
    print(ans)
