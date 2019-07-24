n, k = map(int, input().split())

b = (n // 2) + 1
lo = 0
hi = n
while True:
    r = (2 + b-1) *b // 2
    ans = r - (n - b)
    if ans == k:
        print(n-b)
        exit()
    elif ans < k:
        lo = b
        b = (hi + b) // 2
    else:
        hi = b
        b = (lo + b) // 2



