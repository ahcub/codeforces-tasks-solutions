"""http://codeforces.com/problemset/problem/1000/С"""

n = int(input())

all_dots = set()
stripes = []
for i in range(n):
    a,b = input().split()
    all_dots.add(int(a))
    all_dots.add(int(b))
    stripes.append((int(a), int(b)))

all_dots = sorted(all_dots)

ranges = set()
for a, b in stripes:
    curr_start = a
    for dot in all_dots:
        if a < dot:
            if b < dot:
                break
            if b > dot:
                ranges.add((curr_start, dot-1))
                curr_start = dot

    ranges.add((curr_start, b))

print(sorted(ranges))
