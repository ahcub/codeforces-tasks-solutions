n = int(input())
nominals = [100, 20, 10, 5, 1]
res = 0
for nom in nominals:
    res += n // nom
    n = n % nom
    if n == 0:
        break
print(res)