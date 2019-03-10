from math import ceil

n, k = map(int, input().split())
d = list(map(int, input().split()))

packs = [0]*k
for i in d:
    packs[i%k] += 1

counter = packs[0]//2
if (k % 2) == 0:
    counter += packs[k//2]//2
for i in range(1, ceil(k/2)):
    counter += min(packs[i], packs[k-i])

print(counter*2)
