n = int(input())
a = list(map(int, input().split()))

l_index = 0
r_index = n-1
result = []
if a[l_index] > a[r_index]:
    prev_number = a[r_index]
    r_index -= 1
    result.append('R')
else:
    prev_number = a[l_index]
    l_index += 1
    result.append('L')

while r_index >= l_index:
    if a[l_index] > prev_number and a[r_index] > prev_number:
        if a[l_index] > a[r_index]:
            prev_number = a[r_index]
            r_index -= 1
            result.append('R')
        else:
            prev_number = a[l_index]
            l_index += 1
            result.append('L')
    else:
        if a[l_index] > prev_number:
            prev_number = a[l_index]
            l_index += 1
            result.append('L')
        elif a[r_index] > prev_number:
            prev_number = a[r_index]
            r_index -= 1
            result.append('R')
        else:
            break
print(len(result))
print(''.join(result))