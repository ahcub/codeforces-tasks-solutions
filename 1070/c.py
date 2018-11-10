from collections import defaultdict
from operator import itemgetter


def find_index(list_to_check, index):
    left, right = 0, len(list_to_check) - 1
    while True:
        if left == right:
            return left
        mid = left + ((right - left) // 2)
        if list_to_check[mid] <= index <= list_to_check[mid]:
            return mid
        if list_to_check[mid] > index:
            right = mid
        else:
            left = mid+1


n, k, m = map(int, input().split())


tarif_plans = []
split_dots = set()
for i in range(m):
    l, r, c, p = map(int, input().split())
    tarif_plans.append((l, r+1, c, p))
    split_dots.add(l)
    split_dots.add(r+1)
tarif_plans.sort(key=itemgetter(3))

split_dots = sorted(split_dots)

date_ranges_tarif_plans = defaultdict(list)
for l, r, c, p in tarif_plans:
    lef = find_index(split_dots, l)
    rig = find_index(split_dots, r)
    for index, point in enumerate(split_dots[lef+1:rig+1], lef+1):
        date_ranges_tarif_plans[(split_dots[index-1], point)].append((c, p))

total_price = 0
for (s,e), ac in date_ranges_tarif_plans.items():
    cores = k
    days_diff = e-s
    for av_core, price in ac:
        if av_core > cores:
            total_price += days_diff * cores * price
            break
        else:
            total_price += days_diff * av_core * price
            cores -= av_core

print(total_price)