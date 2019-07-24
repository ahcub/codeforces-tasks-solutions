q = int(input())
m = {
    'R': 'G',
    'G': 'B',
    'B': 'R',
}
rm = {
    'R': 'B',
    'G': 'R',
    'B': 'G',
}
for i in range(q):
    n, k = map(int, input().split())
    bl, br = 1, 1
    bs = 1
    l, r = 1, 1
    strike = 1
    for j in range(1, n):
        if n[j] == m[n[j-1]]:
            strike += 1
            r = j
        else:
            if strike > bs:
                bs = strike
                bl = l
                br = r
            strike = 1
            l, r = 1, 1
    if strike > bs:
        bs = strike
        bl = l
        br = r
    if bs >= k:
        print(0)
    else:
        k -= bs
        cost = [0] * n
        co = 0
        for j in range(l-1, -1, -1):
            tc = m[n[j + 1]]
            if n[j] != tc:
                co += 1
                cost[j] = co
                n[j] = tc
        co = 0
        for j in range(r+1, n):
            tc = m[n[j-1]]
            if n[j] != tc:
                co += 1
                cost[j] = co
                n[j] = tc




