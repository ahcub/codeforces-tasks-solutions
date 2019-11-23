vals = {}
s = 0
for i in range(40):
    k = 3 ** i
    s += k
    vals[k] = s

keys = list(vals.keys())
values = list(vals.values())
q = int(input())
for j in range(q):
    n = int(input())
    for s, k in enumerate(values):
        if n <= k:
            break
    for i in range(s, -1, -1):
        if k - keys[i] >= n:
            k -= keys[i]
            if k == n:
                break
    print(k)
