"""http://codeforces.com/problemset/problem/1000/С"""
from collections import defaultdict
from operator import itemgetter
from random import randint

n = int(input())

all_dots = defaultdict(int)
stripes = []
for i in range(n):
    a,b = input().split()
    all_dots[int(a)] += 1
    all_dots[int(b)] += 1
    stripes.append((int(a), int(b)))

stripes = sorted(stripes)
keys = sorted(all_dots.keys())
all_dots = all_dots

prev_b = None
ranges = defaultdict(int)
for a, b in stripes:
    curr_start = a
    if prev_b is not None and prev_b >= curr_start:
        if (curr_start, prev_b-1) in ranges:
            ranges[(curr_start, prev_b-1)] += 1
        if (prev_b, prev_b) in ranges:
            ranges[(prev_b, prev_b)] += 1
        elif (curr_start, prev_b) in ranges:
            ranges[(curr_start, prev_b)] += 1
        curr_start = prev_b + 1
    if all_dots[curr_start] > 1:
        ranges[(curr_start, curr_start)] += 1
        curr_start = curr_start+1
    if curr_start > b:
        continue
    for dot in keys:
        if curr_start < dot:
            if b < dot:
                prev_b = b
                break
            if b > dot:
                ranges[(curr_start, dot-1)] += 1
                curr_start = dot

    if all_dots[b] > 1:
        ranges[(curr_start, b-1)] += 1
        ranges[(b, b)] += 1
    else:
        ranges[(curr_start, b)] += 1
    prev_b = b

print(ranges)
stripes_counter = {i: 0 for i in range(1, n+1)}
for (a, b), stripes_intersect in ranges.items():
    stripes_counter[stripes_intersect] += 1 + b - a

print(' '.join([str(v) for k, v in sorted(stripes_counter.items(), key=itemgetter(0))]))
