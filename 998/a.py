"""http://codeforces.com/problemset/problem/998/A"""
n = int(input())
packs = list(map(int, input().split()))
lowest_index = packs.index(min(packs)) + 1
if n == 1 or (n == 2 and packs[0] == packs[1]):
    print(-1)
else:
    print(1)
    print(lowest_index)
