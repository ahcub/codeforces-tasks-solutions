n = input()
res = 0
prev_number = 0
for el in reversed(n[1:]):
    if int(el)+prev_number != 10:
        res += 10 - (int(el)+prev_number)
    prev_number = 1

print(res+9)
