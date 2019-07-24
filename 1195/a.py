from math import ceil

n, k = map(int, input().split())

a = [0]*k
for i in range(n):
    a[int(input())-1]+=1

n2 = ceil(n/2)
full = 0
for e in a:
    full += e // 2

if full == n2:
    print(n)
else:
    print(full*2 + n2-full)
