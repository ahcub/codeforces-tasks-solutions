from math import ceil

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
sa = [0]*n
s = 0
l = 0
r = n - 1
for i in range(n):
    s += a[i]
    sa[i] = s

ans = 0


def calc():
    return s - k * ceil((r - l + 1) / m)


while l < r:
    if a[l] < 0:
        l += 1
        continue
    if a[r] < 0:
        r -= 1
        continue
    s = sa[r] - sa[l] + a[l]
    if s > 0:
        na = calc()
        ans = max(ans, na)
    s1 = sa[r] - sa[l + 1]
    s2 = sa[r - 1] - sa[l]

    if s1 > s2:
        l += 1
    else:
        r -= 1

na = calc()
ans = max(ans, na)

print(ans)


'''
11 3 2
1 2 -54 4 5 1 -6 7 8 9 -11

'''
