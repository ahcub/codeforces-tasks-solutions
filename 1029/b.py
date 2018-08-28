"""http://codeforces.com/problemset/problem/1029/B"""

n = int(input())
a = map(int, input().split())

max_iter = 0
current_counter = 0

prev_a = None
for ai in a:
    if prev_a is not None:
        if (prev_a * 2) < ai:
            if max_iter < current_counter:
                max_iter = current_counter
            current_counter = 0
    prev_a = ai
    current_counter += 1

if max_iter < current_counter:
    max_iter = current_counter

print(max_iter)