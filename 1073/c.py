n = input()
moves = input()
x, y = map(int, input().split())

move_vals = {
    'R': ('x', 1),
    'L': ('x', -1),
    'U': ('y', 1),
    'D': ('y', -1),
}
actual_pos = {'x': 0, 'y': 0}
for i in moves:
    direction, shift = move_vals[i]
    actual_pos[direction] += shift

print(actual_pos['x'], actual_pos['y'])

for i in range(len(moves)):
    pass