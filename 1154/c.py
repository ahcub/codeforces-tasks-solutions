a = list(map(int, input().split()))
full = min(a[0] // 3, a[1] // 2, a[2] // 2)

a[0] -= full * 3
a[1] -= full * 2
a[2] -= full * 2
idx = [0, 1, 2, 0, 2, 1, 0]
number_of_days = []
for n in range(7):
    b = list(a)
    day = n
    cur = 0
    while b[idx[day]] > 0:
        b[idx[day]] -= 1
        day = (day + 1) % 7
        cur += 1
    number_of_days.append((full * 7) + cur)
print(max(number_of_days))
