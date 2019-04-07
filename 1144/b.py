n = int(input())
n1 = []
n2 = []
for n in map(int, input().split()):
    if n % 2 == 0:
        n1.append(n)
    else:
        n2.append(n)

if len(n1) > len(n2):
    print(sum(sorted(n1)[:-(len(n2)+1)]))
else:
    print(sum(sorted(n2)[:-(len(n1)+1)]))