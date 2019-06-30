from collections import defaultdict

n = int(input())
s = input()
r = defaultdict(list)
for i, c in enumerate(s):
    r[c].append(i)
m = int(input())
for i in range(m):
    t = input()
    ans = 0
    pos = defaultdict(int)
    for c in t:
        pos[c] += 1
        ans = max(ans, r[c][pos[c]-1])
    print(ans+1)
