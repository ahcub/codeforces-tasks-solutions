n = int(input())

def line_intersect():
    a = 1, 2, 1, 5
    b = 0, 3, 4, 3
    if a[0] <= b[1] <= a[3] and b[0] <= a[1] <= b[3]:
        return True


for i in range(n):
    a, b, c, d = map(int, input().split())

