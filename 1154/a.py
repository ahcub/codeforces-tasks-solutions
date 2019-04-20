x = list(map(int, input().split()))
m = max(x)
res = [str(m - n) for n in x if n != m]
print(' '.join(res))
