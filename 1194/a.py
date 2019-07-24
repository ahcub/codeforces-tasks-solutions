n = int(input())
for i in range(n):
    n, x = map(int, input().split())
    if x < n//2:
        print(2 + (x-1)*2)
    else:
        print(n//2+x)

