# INCOMPLETE
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
    if r_index == l_index:
        result.append('R')
        break
    if a[l_index] > prev_number and a[r_index] > prev_number:
        if a[l_index] > a[r_index]:
            prev_number = a[r_index]
            r_index -= 1
            result.append('R')
        elif a[l_index] == a[r_index]:
            sub_l_index = l_index+1
            sub_res_l = 1
            prev = a[l_index]
            while True:
                if a[sub_l_index] <= prev:
                    break
                sub_res_l += 1
                prev = a[sub_l_index]
                sub_l_index += 1

            sub_r_index = r_index-1
            sub_res_r = 1
            prev = a[r_index]
            while True:
                if a[sub_r_index] <= prev:
                    break
                sub_res_r += 1
                prev = a[sub_r_index]
                sub_r_index -= 1

            if sub_res_l > sub_res_r:
                result.extend(['L']*sub_res_l)
            else:
                result.extend(['R']*sub_res_r)
            break
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