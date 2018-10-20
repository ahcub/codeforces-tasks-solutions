n = int(input())
a = input()
b = input()

ai = [(i, a[i]) for i in range(n) if a[i] != b[i]]
operations_counter = 0
processed_indexes = []
for i, (ind, a_i) in enumerate(ai[:-2]):
    if ind not in processed_indexes:
        if a_i != ai[i+1][1] and (ai[i+1][0] - ind) <= 2:
            processed_indexes.append(ind)
            processed_indexes.append(ai[i+1][0])
            operations_counter += ai[i+1][0] - ind
            continue
        if ai[i + 1][1] != ai[i + 2][1] and (ai[i + 2][0] - ai[i + 1][0]) <= 2:
            processed_indexes.append(ai[i + 1][0])
            processed_indexes.append(ai[i + 2][0])
            operations_counter += ai[i + 2][0] - ai[i + 1][0] + 1
            continue
        operations_counter += 1

print(operations_counter)
