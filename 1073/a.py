n = input()
a = input()

diff_str = []
for i in a.strip():
    if i not in diff_str:
        diff_str.append(i)
        if len(diff_str) == 2:
            print('YES')
            print(''.join(diff_str))
            break
    else:
        diff_str = [i]
else:
    print('NO')
