from collections import defaultdict


sa = input().split()
groups = defaultdict(list)
for el in sa:
    groups[el[-1]].append(int(el[0]))

test_arrays = []
for i in range(1, 7):
    test_arrays.append([i, i+1, i+2])

min_card = 2
for elements in groups.values():
    els = sorted(elements)
    for i in range(1, 10):
        count = els.count(i)
        if count == 3:
            print(0);exit()
        if count == 2:
            print(1);exit()
    for ta in test_arrays:
        m = 3
        for i in ta:
            if i in els:
                m-=1
        if m < min_card:
            min_card = m
            if m == 0:
                print(0);exit()
print(min_card)
