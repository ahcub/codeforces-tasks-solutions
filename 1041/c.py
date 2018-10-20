n, m, d = map(int, input().split())
a = list(map(int, input().split()))

days_map = {}
for t in sorted(a):
    for i, dy in enumerate(days):
        if dy <= t:
            days[i] = t + 1 + d
            days_map[t] = i + 1
            break
    else:
        days.append(t + 1 + d)
        days_map[t] = len(days)

print(len(days))
print(' '.join([str(days_map[el]) for el in a]))
