#TODO
n,m = map(int, input().split())
user_groups = []
groups = []
for i in range(m):
    g = set(list(map(int, input().split()))[1:])
    if g:
        groups.append(g)


new_groups = [[]]*m
for i, g1 in enumerate(groups):
    for j, g2 in enumerate(groups):
        if i != j:
            if g1 ^ g2:
                new_groups[i].append(j)

