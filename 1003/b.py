a, b, x = map(int, input().split())
n = a+b
result_string = '0'*a + '1'*b
if x in [0, 1]:
    print(result_string)
else:
    result_string = list(result_string)

    prev_char = None
    for char in result_string:
        if char != prev_char and prev_char is not None:
            pass
        else:

    # x_ = x % 2
    # if x_ == 0:
    #     result_string[0], result_string[b] = result_string[b], result_string[0]
    #     for i in range(x_, (x // 2) + x_, 2):
    #         result_string[i + 1], result_string[i + n - b] = result_string[i + n - b], result_string[i + 1]
    # else:
    #     for i in range(0, (x // 2), 2):
    #         result_string[i+1], result_string[i+n-b] = result_string[i+n-b], result_string[i+1]

    # result_string[0], result_string[a] = result_string[a], result_string[0]
    # if a != 1 and b != 1:
    #     x -= 1
    # x -= 1
    # right_one_i = 1
    # while x != 0:
    #     if x == 1:
    #         if a > 1:
    #             result_string[right_one_i-1], result_string[right_one_i] = result_string[right_one_i], result_string[right_one_i-1]
    #         else:
    #             result_string[-1], result_string[-2] = result_string[-2], result_string[-1]
    #         x -= 1
    #     else:
    #         result_string[right_one_i+2], result_string[right_one_i + a] = result_string[right_one_i + a], result_string[right_one_i+2]
    #         x -= 2
    #         right_one_i += 3
    print(''.join(result_string))

nn = 0
prev_char = None
for char in result_string:
    if char != prev_char and prev_char is not None:
        nn += 1
    prev_char = char

print(nn)