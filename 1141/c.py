n = int(input())
p = list(map(int, input().split()))


unused_numbers = set()
res = [0]
prev_el = 0
for i in range(n-1):
    prev_el = prev_el + p[i]
    res.append(prev_el)
m = 1 - min(res)
for i in range(n):
    res[i] += m

if sorted(res) == list(range(1, n+1)):
    print(' '.join([str(el) for el in res]))
else:
    print(-1)