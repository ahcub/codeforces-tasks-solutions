n = int(input())
a = list(map(int, input()))
f = {i: el for i, el in enumerate(map(int, input().split()), 1)}

big_changes_made = False
for i, el in enumerate(a):
    if el < f[el]:
        a[i] = f[el]
        big_changes_made = True
    elif el != f[el]:
        if big_changes_made:
            break
print(''.join(map(str, a)))
