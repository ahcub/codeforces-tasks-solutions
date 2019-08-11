n = int(input())
x = [0]*10

for c in input():
    if c == 'L':
        for i in range(10):
            if x[i] == 0:
                x[i] = 1
                break
    elif c == 'R':
        for i in range(9, -1, -1):
            if x[i] == 0:
                x[i] = 1
                break
    else:
        x[int(c)] = 0

print(*x, sep='')
