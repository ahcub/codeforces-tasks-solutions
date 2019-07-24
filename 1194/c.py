q = int(input())


def process():
    s = input()
    t = input()
    p = sorted(input())
    ti = 0
    missing = []
    for c in s:
        if ti >= len(t):
            return False
        while c != t[ti]:
            missing.append(t[ti])
            ti+=1
            if ti >= len(t):
                return False
        ti+=1

    pi = 0
    for c in sorted(missing+list(t[ti:])):
        if pi >= len(p):
            return False
        while c != p[pi]:
            pi+=1
            if pi >= len(p):
                return False
        pi+=1
    return True


for i in range(q):
    print('yes' if process() else 'no')
