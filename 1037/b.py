"""http://codeforces.com/problemset/problem/1037/B"""

n, s = map(int, input().split())
a = map(int, input().split())
a = sorted(a)
if n == 1:
    print(abs(s - a[0]))
else:
    index = (n // 2)
    if a[index] == s:
        print(0)
    elif a[index] < s:
        k = [s - el for el in a[index:] if el < s]
        print(sum(k))
    else:
        k = [el - s for el in a[:index+1] if el > s]
        print(sum(k))

