n,m  = map(int, input().split())
a = list(map(int, input().split()))
aa = sorted(set(a))
aaa = [0] * len(aa)

def find(e, l, r, g):
    mid = l + ((r - l) // 2)
    if aa[mid] == e:
        aaa[mid] += g
    elif r == l:
        aaa[r] += g
    elif aa[mid] < e:
        find(e, mid, r, g)
    else:
        find(e, l, mid, g)

for i in range(m):
    d,g = map(int, input().split())
    if d <= aa[-1]:
        find(d, 0, n-1, g)

t = 0
for i, e in enumerate(aaa):
    t += e
    aaa[i] = t
d = dict(zip(aa, aaa))
for e in a:
    print(d[e], end=' ')
