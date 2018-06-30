"""http://codeforces.com/problemset/problem/1000/A"""

n = int(input())
a = []
for i in range(n):
    a.append(input())


for i in range(n):
    b_s = input()
    if b_s in a:
        a.remove(b_s)

print(len(a))
