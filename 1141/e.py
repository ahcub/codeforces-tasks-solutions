from itertools import accumulate
H, r = map(int, input().split())
d = list(map(int, input().split()))
cum_diff = list(accumulate(d))
min_val = min(cum_diff)
rounds_when_dead = []
last_value = cum_diff[-1]
for i, el in enumerate(cum_diff, 1):
    if el > 0:
        continue
    elif -el >= H:
        rounds_when_dead.append(i)
    else:
        if last_value >= 0:
            continue
        else:
            c = (H + min_val) // -last_value
            if ((H + min_val) % -last_value) != 0:
                c += 1
            if -((c*last_value) + el) >= H:
                rounds_when_dead.append(i + c * r)

if rounds_when_dead:
    print(min(rounds_when_dead))
else:
    print(-1)