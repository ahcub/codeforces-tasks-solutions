n, m = map(int, input().split())
a = [0] * n
ordered = []
unordered = []
for i in range(m):
    list1 = list(map(int, input().split()))
    if list1[0] == 0:
        unordered.append(list1)
    else:
        ordered.append(list1)

for t, l, r in ordered:
    for i in range(l, r):
        a[i] = t

for t, l, r in unordered:
    unset = any(e == 0 for e in a[l:r])
    if not unset:
        print('NO')
        exit()

print('YES')
v = 100000
for e in a:
    if e == 1:
        v += 1
    else:
        v -= 1
    print(v, end=' ')
