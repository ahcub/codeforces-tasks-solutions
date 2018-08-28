"""http://codeforces.com/problemset/problem/1029/A"""

n, k = map(int, input().split())
t = input()
merge_index = None
for i in range(1, n):
    if t[i:] == t[:-i]:
        merge_index = i
        break

if merge_index is not None:
    res = []
    for i in range(k):
        res.append(t[:merge_index])
    res.append(t[merge_index:])
else:
    res = [t] * k
print(''.join(res))