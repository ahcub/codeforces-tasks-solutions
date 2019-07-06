n = int(input())
a = sorted(list(map(int, input().split())))

if a[-1] >= a[-2] + a[-3]:
    print('NO')
else:
    print('YES')
    print(a[-3], a[-1], a[-2], end=' ')
    print(*a[-4::-1])
