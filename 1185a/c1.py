import bisect
n, m = map(int, input().split())
t = list(map(int, input().split()))
max_numbers = []
total_sum = 0
ans = []
for s in t:
    total_sum += s
    if total_sum <= m:
        ans.append(0)
    else:
        total_sub = 0
        num = 0
        for e in max_numbers[::-1]:
            total_sub += e
            num += 1
            if total_sum - total_sub <= m:
                ans.append(num)
                break

    bisect.insort(max_numbers, s)

print(*ans)
