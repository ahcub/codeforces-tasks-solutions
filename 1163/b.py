#TODO
from collections import defaultdict

n = int(input())
u = list(map(int, input().split()))

counter = defaultdict(int)
for v in u:
    counter[v] += 1

prefix_c = n
vals = defaultdict(int)
for v in counter.values():
    vals[v] += 1


while True:
    if len(counter) == 1:
        break
    vvs = list(vals.values())
    kvs = list(vals.keys())
    if len(vvs) == 1 and kvs[0] == 1:
        break
    if len(vals) == 2:
        if kvs[0] == 1 or kvs[1] == 1:
            break
        if vvs[0] - vvs[1] == 1 and kvs[0] == 1 or vvs[1] - vvs[0] == 1 and kvs[1] == 1:
            break

    i = prefix_c - 1
    vals[counter[u[i]]] -= 1
    if vals[counter[u[i]]] == 0:
        del vals[counter[u[i]]]
    counter[u[i]] -= 1
    if counter[u[i]] == 0:
        del counter[u[i]]
    prefix_c -= 1

print(prefix_c)