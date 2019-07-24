from collections import defaultdict

n, m, k = map(int, input().split())
mp = defaultdict(dict)
for i in range(m):
    x, y, w = map(int, input().split())
    mp[x][y]=w

for i in range(n):

