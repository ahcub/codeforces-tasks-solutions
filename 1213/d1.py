from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

vals = defaultdict(list)
ctn = defaultdict(int)

for el in a:
    cur = 0
    while el > 0:
        vals[el].append(cur)
        ctn[el] += 1
        el //= 2
        cur += 1

ans = 99999999999
for kk, ct in ctn.items():
    if ct >= k:
        ans = min(ans, sum(sorted(vals[kk])[:k]))
print(ans)
