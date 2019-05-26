n,m = map(int, input().split())
groups = []
user_passed = 1 << n+1
for i in range(m):
    g = 0
    for user in list(map(int, input().split()))[1:]:
        g |= 1 << user-1
    if g:
        groups.append(g)


def get_indexes(number):
    bits = '{0:b}'.format(number)[::-1]
    return [i for i, el in enumerate(bits) if el == '1']


user_groups = [0] * n
for gr in groups:
    for i in get_indexes(gr):
        user_groups[i] |= gr

groups_registry = []


def wave(user_id, processed_users=None, main=True):
    if main:
        for gr, c in groups_registry:
            if 1 << user_id & gr:
                return c
    if processed_users is None:
        processed_users = [1 << user_id]
    for user in get_indexes(user_groups[user_id]):
        if not (1 << user & processed_users[0]):
            processed_users[0] |= 1 << user
            wave(user, processed_users, main=False)
    counter = len(get_indexes(processed_users[0]))
    if main:
        groups_registry.append((processed_users[0], counter))
    return counter


print(' '.join(str(wave(i)) for i in range(n)))
