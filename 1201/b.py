n = int(input())
a = list(map(int, input().split()))
s = sum(a)
m = max(a)
if s % 2 == 1 or m > (s / 2):
    print('NO')
else:
    print('YES')
