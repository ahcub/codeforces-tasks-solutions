n = int(input())


def iteration():
    f = input()
    s = input()
    s_pos = 0
    prev_c = f[0]
    for i, c in enumerate(f):
        while c != s[s_pos]:
            if s[s_pos] != prev_c:
                return 'NO'
            s_pos += 1
            if s_pos >= len(s):
                return 'NO'
        prev_c = c
        s_pos += 1
        if i!=len(f)-1 and s_pos >= len(s):
            return 'NO'
    if s_pos < len(s):
        for c in s[s_pos:]:
            if c != s[s_pos-1]:
                return 'NO'
    return 'YES'


for i in range(n):
    print(iteration())
