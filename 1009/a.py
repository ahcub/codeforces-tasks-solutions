"""http://codeforces.com/problemset/problem/1009/A"""
n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
a = list(map(int, input().split()))

bought_games = 0
ci = 0
ai = 0
while ci < len(c) and ai < len(a):
    if a[ai] >= c[ci]:
        bought_games += 1
        ai += 1
    ci += 1

print(bought_games)