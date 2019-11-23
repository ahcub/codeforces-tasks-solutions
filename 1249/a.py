q = int(input())
for j in range(q):
    n = int(input())
    students = sorted(map(int, input().split()))
    for i in range(1, len(students)):
        if students[i] - students[i-1] == 1:
            print(2)
            break
    else:
        print(1)
