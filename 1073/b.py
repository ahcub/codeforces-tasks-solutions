n = input()
a = input().split()
b = input().split()
d = {el: i for i, el in enumerate(a)}
diff_b = []
prev_number = 0
for i, el in enumerate(b):
    f = d[el]
    if prev_number < i:
        t = max(f - i + 1, 0)
    else:
        t = max(f - prev_number + 1, 0)
    prev_number += t

    diff_b.append(str(t))

print(' '.join(diff_b))