n, m = map(int, input().split())

f = []
all_dots = set()
horizontals = []

for i in range(n):
    row = input()
    line = []
    for j in range(m):
        if row[j] == '*':
            all_dots.add((i, j))
            line.append((i, j))
        else:
            if line and len(line) > 1:
                horizontals.append(line)
                line = []
            else:
                line = []
    if line and len(line) > 1:
        horizontals.append(line)
    f.append(row)

t_f = list(map(list, zip(*f)))
verticals = []
for j in range(m):
    row = t_f[j]
    line = []
    for i in range(n):
        if row[i] == '*':
            line.append((i, j))
        else:
            if line and len(line) > 1:
                verticals.append(line)
                line = []
            else:
                line = []
    if line and len(line) > 1:
        verticals.append(line)

if len(horizontals) > 1 or len(horizontals) == 0:
    print('NO')
    exit()

if len(verticals) > 1 or len(verticals) == 0:
    print('NO')
    exit()

h = set(horizontals[0])
v = set(verticals[0])
cross_dots = h|v
cross = h & v
if cross:
    if all_dots - cross_dots:
        print('NO')
        exit()
    if len(verticals[0]) < 3 or len(horizontals[0]) < 3:
        print('NO')
        exit()
    i, j = cross.pop()
    if f[i][j] == '*' and f[i+1][j] == '*' and f[i][j+1] == '*' and f[i][j-1] == '*' and f[i+1][j] == '*':
        print('YES')
        exit()
print('NO')



