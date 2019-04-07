from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
c = defaultdict(int)
for el in a:
    c[el] += 1

most_p, most_p_amount = 0, 0
for num, amount in c.items():
    if amount > most_p_amount:
        most_p = num
        most_p_amount = amount

operations = []
most_p_i = a.index(most_p)

for i in range(most_p_i, len(a)-1):
    if most_p > a[i+1]:
        operations.append((1, i+1, i))
    if most_p < a[i+1]:
        operations.append((2, i+1, i))
for i in range(most_p_i, 0, -1):
    if most_p > a[i-1]:
        operations.append((1, i-1, i))
    if most_p < a[i-1]:
        operations.append((2, i-1, i))

print(len(operations))
for op, i1, i2 in operations:
    print(op, i1+1, i2+1)
