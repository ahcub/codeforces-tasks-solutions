n, m = map(int, input().split())

if (m % n) != 0:
    print(-1)
else:
    res = m // n
    counter = 0
    while res != 1:
        if (res % 2) == 0:
            res //= 2
            counter += 1
        elif (res % 3) == 0:
            res //= 3
            counter += 1
        else:
            print(-1)
            exit()
    print(counter)
