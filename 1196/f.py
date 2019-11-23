n, m, k = map(int, input().split())
min_paths = [0]*(n+1)
for i in range(m):
    x, y, w = map(int, input().split())
    min_paths[x]=min(min_paths[x],w) if min_paths[x] != 0 else w
    min_paths[y]=min(min_paths[y],w) if min_paths[y] != 0 else w

print(sorted(min_paths)[k])
