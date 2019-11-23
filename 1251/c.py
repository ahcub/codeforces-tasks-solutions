q = int(input())

for _ in range(q):
    d = input()
    a = []
    b = []
    for el in d:
        n = int(el)
        if (n % 2) == 0:
            a.append(n)
        else:
            b.append(n)
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(str(a[i]))
            i += 1
        else:
            res.append(str(b[j]))
            j += 1
    if i < len(a):
        res.extend([str(e) for e in a[i:]])
    else:
        res.extend([str(e) for e in b[j:]])
    print(''.join(res))
