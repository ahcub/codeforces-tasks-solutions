q = int(input())
for j in range(q):
    n = int(input())
    students = list(map(int, input().split()))
    a = set(students)
    ans = {}
    while a:
        route = []
        ai = a.pop()
        cur = students[ai-1]
        route.append(ai)
        while cur != ai:
            route.append(cur)
            a.discard(cur)
            cur = students[cur-1]
        ans.update({r: len(route) for r in route})
    print(*[ans[s] for s in students])
