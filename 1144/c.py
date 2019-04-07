n = int(input())
a = sorted(map(int, input().split()))

n1, n2 = [], []

for i, el in enumerate(a):
    if i > 1 and el == a[i-1] == a[i-2]:
        print('NO')
        exit()
    if el == a[i-1]:
        n2.append(el)
    else:
        n1.append(el)

print('YES')
print(len(n1))
print(' '.join([str(n) for n in n1]))
print(len(n2))
print(' '.join(reversed([str(n) for n in n2])))
