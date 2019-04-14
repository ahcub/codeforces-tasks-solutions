n, t = map(int, input().split())
buses = {}
for i in range(1, n+1):
    s, d = map(int, input().split())
    ts = max(0, (t - s))
    bus_time = ts // d
    if (ts % d) != 0:
        bus_time += 1
    buses[s + (bus_time*d)] = i

print(buses[min(buses.keys())])
