a,b,c,d = map(int, input().split())
mi, mid, ma = sorted((a,b,c))
secs = max(-((mid - mi) - d), 0)
secs += max(-((ma - mid) - d), 0)
print(secs)