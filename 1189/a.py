n = int(input())
s = input()
if n%2 != 0 or s.count('0') != n // 2:
    print(1)
    print(s)
else:
    print(2)
    print(s[:-1], s[-1])

