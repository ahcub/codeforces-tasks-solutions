# TODO. this solution is incomplete

n = int(input())
s = input()
if n % 2 != 0 or '(' in s[-2:]:
    print(':(')
elif n == 0:
    print()
else:
    result1 = []
    result2 = []
    left = s[:len(s) // 2]
    right = s[len(s) // 2:][::-1]
    n1 = left.count('(') - left.count(')')
    n2 = right.count(')') - right.count('(')
    for a in left:
        if a == '?':
            if n1 > 1:
                n1 -= 1
                result1.append(')')
            else:
                n1 += 1
                result1.append('(')
        else:
            result1.append(a)
    for a in right:
        if a == '?':
            if n2 > 1:
                n2 -= 1
                result2.append('(')
            else:
                n2 += 1
                result2.append(')')
        else:
            result2.append(a)
    if n1 != n2:
        print(':(')
    else:
        print(''.join(result1) + ''.join(result2[::-1]))