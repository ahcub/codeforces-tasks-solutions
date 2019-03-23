from collections import defaultdict, deque

n = input()
left, right = input(), input()


left_location_map = defaultdict(list)
for i, l in enumerate(left, 1):
    left_location_map[l].append(i)

right_location_map = defaultdict(list)
right_count = defaultdict(int)
for i, l in enumerate(right, 1):
    right_location_map[l].append(i)

pairs = []
for l in left_location_map.keys():
    if l != '?' and left_location_map[l]:
        if l in right_location_map:
            p_n = min(len(left_location_map[l]), len(right_location_map[l]))
            pairs.extend(zip(left_location_map[l][:p_n], right_location_map[l][:p_n]))
            left_location_map[l] = left_location_map[l][p_n:]
            right_location_map[l] = right_location_map[l][p_n:]

for l in left_location_map.keys():
    r = '?'
    if l != '?' and left_location_map[l]:
        if r in right_location_map:
            p_n = min(len(left_location_map[l]), len(right_location_map[r]))
            pairs.extend(zip(left_location_map[l][:p_n], right_location_map[r][:p_n]))
            left_location_map[l] = left_location_map[l][p_n:]
            right_location_map[r] = right_location_map[r][p_n:]


for r in right_location_map:
    l = '?'
    if r != '?' and right_location_map[r]:
        if l in left_location_map:
            p_n = min(len(left_location_map[l]), len(right_location_map[r]))
            pairs.extend(zip(left_location_map[l][:p_n], right_location_map[r][:p_n]))
            left_location_map[l] = left_location_map[l][p_n:]
            right_location_map[r] = right_location_map[r][p_n:]


l = '?'
r = '?'
if r in right_location_map and l in left_location_map:
    p_n = min(len(left_location_map[l]), len(right_location_map[r]))
    if p_n > 0:
        pairs.extend(zip(left_location_map[l][:p_n], right_location_map[r][:p_n]))
        left_location_map[l] = left_location_map[l][p_n:]
        right_location_map[r] = right_location_map[r][p_n:]
        if not left_location_map[l]:
            del left_location_map[l]
        if not right_location_map[r]:
            del right_location_map[r]

print(len(pairs))
for l, r in pairs:
    print(l, r)
