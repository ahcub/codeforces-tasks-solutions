from collections import defaultdict

n = int(input())
d = defaultdict(int)
desired_map = []
tree = defaultdict(list)
for i in range(n-1):
    sa = input().split()
    d[sa[0]] += 1
    d[sa[1]] += 1
    sa[2] = int(sa[2])
    desired_map.append(sa)
    tree[sa[0]].append(sa[1])
    tree[sa[1]].append(sa[0])

for v in d.values():
    if v == 2:
        print('NO')
        exit()


def get_leaf(node, exclude_leaf, *exclude):
    if len(tree[node]) == 1:
        return node
    for el in tree[node]:
        if el not in exclude and el != exclude_leaf:
            if len(tree[el]) == 1:
                return el
            else:
                return get_leaf(el, node, exclude_leaf)
    raise Exception('no number')

ans = []
print('YES')
if n == 2:
    print(1)
    print(*desired_map[0])
else:
    for v, u, w in desired_map:
        if len(tree[v]) != 1 and len(tree[u]) != 1:
            a1 = get_leaf(v, u)
            a2 = get_leaf(v, a1, u)
            b1 = get_leaf(u, v)
            b2 = get_leaf(u, b1, v)
        else:
            if len(tree[v]) == 1:
                a1 = a2 = v
                root = tree[v][0]
                possible_directions = [el for el in tree[root] if el != u]
                b1 = get_leaf(possible_directions[0], root)
                b2 = get_leaf(possible_directions[1], root)
            else:
                b1 = b2 = u
                root = tree[u][0]
                possible_directions = [el for el in tree[root] if el != u]
                a1 = get_leaf(possible_directions[0], root)
                a2 = get_leaf(possible_directions[1], root)

        if a1 == a2:
            ans.append((v, b1, w//2))
            ans.append((v, b2, w//2))
            ans.append((b1, b2, -w//2))
        elif b1 == b2:
            ans.append((u, a1, w//2))
            ans.append((u, a2, w//2))
            ans.append((a1, a2, -w//2))
        else:
            ans.append((a1, b1, w//2))
            ans.append((a2, b2, w//2))
            ans.append((a1, a2, -w//2))
            ans.append((b1, b2, -w//2))
    print(len(ans))
    for el in ans:
        print(*el)
