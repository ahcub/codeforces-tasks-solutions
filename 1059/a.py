n, L, a = map(int, input().split())
total_breaks = 0
curr_pos = 0
for i in range(n):
    t, l = map(int, input().split())
    total_breaks += (t - curr_pos) // a
    curr_pos = t+l
total_breaks += (L - curr_pos) // a
print(total_breaks)
