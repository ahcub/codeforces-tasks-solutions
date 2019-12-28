for _ in range(int(input())):
    l, m, r = sorted(map(int, input().split()))
    print((l+m+r)//2 if l + m > r else l+m)
