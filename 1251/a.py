q = int(input())

for _ in range(q):
    c = input()
    working_keys = set()
    p = c[0]
    co = 1
    for el in c[1:]:
        if el == p:
            co += 1
        else:
            if (co % 2) == 1:
                working_keys.add(p)
            p = el
            co = 1
    if (co % 2) == 1:
        working_keys.add(p)
    print(''.join(sorted(working_keys)))
