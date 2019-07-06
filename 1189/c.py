n = int(input())
a = list(map(int, input().split()))
m = int(input())
aa = [1]*n
total = 0
for i, el in enumerate(a):
    total += el
    aa[i] = total

for i in range(m):
    l, r = map(int, input().split())
    print((aa[r-1] - (aa[l-2] if l > 1 else 0)) // 10)

