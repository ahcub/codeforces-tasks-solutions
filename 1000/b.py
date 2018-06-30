"""http://codeforces.com/problemset/problem/1000/B"""

n, m = input().split()
n = int(n)
m = int(m)
ai = [int(a) for a in input().split()]

if not(len(ai) == 2 and (ai[1] - ai[0]) == 1):
    ai = [0] + ai + [m]

    state = True
    shining_time_orig= 0
    for i, a in enumerate(ai[1:-1], 1):
        if state:
            shining_time_orig += ai[i] - ai[i - 1]
            state = False
        else:
            state = True
    if state:
        shining_time_orig += ai[-1] - ai[-2]

    ai_c = list(ai)
    ai_c.insert(2, ai_c[1]+1)
    state = True
    shining_time_c= 0
    for i, a in enumerate(ai_c[1:-1], 1):
        if state:
            shining_time_c += ai_c[i] - ai_c[i - 1]
            state = False
        else:
            state = True
    if state:
        shining_time_c += ai_c[-1] - ai_c[-2]

    state = True
    saved_state = None
    biggest_gap = 0
    biggest_gap_index = None
    for i, a in enumerate(ai[1:-1], 1):
        if state:
            state = False
        else:
            state = True

        gap = ai[i] - ai[i-1]
        if gap > 1:
            if gap > biggest_gap or (gap == biggest_gap and not state):
                biggest_gap = gap
                biggest_gap_index = i
                saved_state = state

    if biggest_gap:
        if saved_state:
            ai.insert(biggest_gap_index, ai[biggest_gap_index-1]+1)
        else:
            ai.insert(biggest_gap_index, ai[biggest_gap_index]-1)
else:
    ai = [0] + ai + [m]
    shining_time_c = 0
    shining_time_orig = 0
state = True
shining_time = 0
for i, a in enumerate(ai[1:-1], 1):
    if state:
        shining_time += ai[i] - ai[i-1]
        state = False
    else:
        state = True

if state:
    shining_time += ai[-1] - ai[-2]

print((max(shining_time, shining_time_c, shining_time_orig)))
