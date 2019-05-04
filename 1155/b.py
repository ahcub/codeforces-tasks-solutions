n = int(input())
s = input()
to_change = s[:-10]
eights = to_change.count('8')
diff = len(to_change) - eights

if diff <= eights:
    print('YES')
else:
    print('NO')