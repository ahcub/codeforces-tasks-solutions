"""http://codeforces.com/problemset/problem/1040/B"""

n, k = map(int, input().split())

step = k * 2 + 1
ranges = n // step

if k == 0:
    print(n)
    print(' '.join([str(i) for i in range(1, n+1)]))
elif k >= n:
    print(1)
    print(1)
else:
    turn_points = []
    for i in range(1, n+1, step):
        turn_points.append(i + k)

    if turn_points[-1] > n:
        a = turn_points[-1] - n
        turn_points = [str(el - a) for el in turn_points]
    else:
        turn_points = [str(el) for el in turn_points]
    print(len(turn_points))
    print(' '.join(turn_points))
