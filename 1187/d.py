n = int(input())
for i in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    diff_start = None
    diff_end = None
    for i in range(m):
        if a[i] != b[i]:
            if diff_start is None:
                diff_start = diff_end == i
            else:
                if b[i] < b[i-1]:
                    print('no')
                    exit()
                diff_end += 1
        else:
            if b[i] < b[i-1]:
                if diff_start is not None:
                    if sorted(b[])
