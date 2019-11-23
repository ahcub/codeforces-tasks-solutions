q = int(input())

for _ in range(q):
    d = int(input())
    a = 0
    b = 0
    c = 0
    for i in range(d):
        g = input()
        c += len(g)
        for el in g:
            if el == '0':
                a += 1
            else:
                b += 1
    if (c % 2) == 0:
        if (a % 2) == 1:
            print(d - 1)
        else:
            print(d)
    else:
        print(d)

