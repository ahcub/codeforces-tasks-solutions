n, m = map(int, input().split())

alt_c1 = 0
alt_c2 = 0
vals_1 = [0] * (n+1)
vals_2 = [0] * (n+1)
a, b = map(int, input().split())
for i in range(m-1):
    ai, bi = map(int, input().split())
    if ai != a and bi != a:
        vals_1[ai] += 1
        vals_1[bi] += 1
        alt_c1+=1

    if ai != b and bi != b:
        vals_2[ai] += 1
        vals_2[bi] += 1
        alt_c2+=1

if max(vals_1) == alt_c1 or max(vals_2) == alt_c2:
    print('YES')
    exit()

print('NO')
