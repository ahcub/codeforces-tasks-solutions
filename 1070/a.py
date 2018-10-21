from collections import deque

d, s = map(int, input().split())
dis = [[None for i in range(s+1)] for j in range(d)]


def bfs():
    Q = deque()
    dis[0][0] = 0
    Q.append((0, 0))
    while Q:
        x, y = Q.popleft()
        for i in range(10):
            xx = (10 * x + i) % d
            yy = y + i
            if yy > s or dis[xx][yy] is not None:
                continue
            dis[xx][yy] = x, y, i
            Q.append((xx, yy))


def out(x, y, res=[]):
    if x == 0 and y == 0:
        return
    else:
        out(dis[x][y][0], dis[x][y][1])
        res.append(str(dis[x][y][2]))
    return res


bfs()
if dis[0][s] is None:
    print(-1)
else:
    print(''.join(out(0, s)))

