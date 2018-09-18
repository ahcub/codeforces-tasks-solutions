"""http://codeforces.com/problemset/problem/1041/A"""

i = int(input())
b = list(map(int, input().split()))
print(max(b) - min(b) - len(b) + 1)