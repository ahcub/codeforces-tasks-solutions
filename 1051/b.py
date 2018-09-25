"""http://codeforces.com/problemset/problem/1051/B"""
l, r = map(int, input().split())
print('YES')
for a, b in zip(range(l, r, 2), range(l+1, r+1, 2)):
    print(a, b)