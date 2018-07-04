n = int(input())
exits = list(map(int, input().split()))
i1 = len(exits)
earliest_index = None
earliest_val = None
for i, val in enumerate(exits):
    exits_ = val // i1
    left = val % i1
    if left > i:
        exits_ += 1
    if earliest_val is None or earliest_val > exits_:
        earliest_val = exits_
        earliest_index = i
print(earliest_index+1)
