for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    left = None
    for i, el in enumerate(a, 1):
        if el % 2 == 0:
            print(1)
            print(i)
            break
        else:
            if left is None:
                left = i
            else:
                print(2)
                print(left, i)
                break
    else:
        print(-1)
