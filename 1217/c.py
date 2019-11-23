q = int(input())

for j in range(q):
    c = 0
    s = input()
    for i in range(1, int(s, 2)+1):
        ss = format(i, "#0%sb" % (i+2))[2:]
        for k in range(len(s) - (len(ss)-1)):
            c += ss == s[k:k + len(ss)]
    print(c)
