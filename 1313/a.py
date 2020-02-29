# 1
# 2
# 3
# 12
# 13
# 23
# 123


for _ in range(int(input())):
    food = sorted(list(map(int, input().split())))
    if food[0] == 0:
        if food[1] == 0:
            if food[2] == 0:
                print(0)
            else:
                print(1)
        else:
            if food[1] > 1:
                print(3)
            else:
                print(2)
    else:
        if food[0] >= 4:
            print(7)
        elif food[0] >= 3:
            print(6)
        elif food[0] >= 2:
            if food[2] >= 3:
                print(5)
            else:
                print(4)
        else:
            if food[1] >= 2:
                print(4)
            else:
                print(3)
