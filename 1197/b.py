n = int(input())
a = list(map(int, input().split()))


up = True
prev = 0
for el in a:
    if el > prev or prev == 0:
        if not up:
            print('no')
            exit()
    else:
        up = False

    prev = el
print('yes')
