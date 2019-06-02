n, sd, ed, sv, ev = map(int, input().split())

t_s_d = [(i, s%n) for i, s in enumerate(range(sd, ed+1 if ed > sd else ed+n+1))]
t_s_v = [(i, s%n) for i, s in enumerate(range(sv, ev-1 if ev < sv else ev-n-1, -1))]

if set(t_s_d) & set(t_s_v):
    print('YES')
else:
    print('NO')