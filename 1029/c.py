from operator import itemgetter

n = int(input())
lines = sorted([list(map(int, input().split())) for i in range(n)], key=itemgetter(0))


if lines[0][1] <= lines[1][0]:
    lines.pop(0)
elif lines[-1][0] >= lines[-2][1]:
    lines.pop(-1)
else:
    lowest_width_id = None
    lowest_width = None
    for index, (a, b) in enumerate(lines):
        if lowest_width is None:
            lowest_width = b - a
            lowest_width_id = index
        else:
            if (b - a) < lowest_width:
                lowest_width = b - a
                lowest_width_id = index
    first_width = (lines[0][1] - lines[1][0])
    last_width = (lines[-2][1] - lines[-1][0])
    pooped = False
    if first_width < last_width:
        if first_width < lowest_width:
            lines.pop(0)
            pooped = True
    elif first_width > last_width:
        if last_width < lowest_width:
            lines.pop(-1)
            pooped = True

    if not pooped:
        lines.pop(lowest_width_id)

left = None
right = None
for a, b in lines:
    if left is None or left < a:
        left = a
    if right is None or right > b:
        right = b

print(max(0, right - left))