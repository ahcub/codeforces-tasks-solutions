"""http://codeforces.com/problemset/problem/1040/A"""

n, a, b = map(int, input().split())
c = list(map(int, input().split()))

t = {
    0: a,
    1: b,
}

total_price = 0
for i in range(n):
    back_i = n - i - 1
    if back_i >= i:
        if c[i] == c[back_i] or c[i] == 2 or c[back_i] == 2:
            if c[i] == 2 and c[back_i] == 2:
                if back_i == i:
                    total_price += min(a, b)
                else:
                    total_price += 2 * min(a, b)
            elif c[i] == 2:
                total_price += t[c[back_i]]
            elif c[back_i] == 2:
                total_price += t[c[i]]
        else:
            print(-1)
            exit()
print(total_price)
