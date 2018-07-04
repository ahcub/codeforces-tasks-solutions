from collections import defaultdict

n = int(input())
r = defaultdict(int)
for i in map(int, input().split()):r[i] += 1
print(max(r.values()))
