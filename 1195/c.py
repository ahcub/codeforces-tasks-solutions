_ = int(input())
n = [list(map(int, input().split())), list(map(int, input().split()))]
d = (0, 0)
for i in range(_):
    d = (max(d[0], d[1] + n[0][i]), max(d[1], d[0] + n[1][i]))
print(max(d[0], d[1]))

