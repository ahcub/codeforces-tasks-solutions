n = int(input())

black_listed = []
white_listed = []
multiplication = [2**24, 2**16, 2**8, 1]
ranges = {2 ** i: str(32-i) for i in range(0, 33)}
for i in range(n):
    address_str = input()
    is_black_list = address_str[0] == '-'
    if '/' in address_str:
        clean_addr, x = address_str[1:].split('/')
        x = int(x)
    else:
        clean_addr, x = address_str[1:], 32
    addr_num = 0
    for multipier, num in zip(multiplication, map(int, clean_addr.split('.'))):
        addr_num += multipier * num
    address_range = pow(2, 32-x)
    if is_black_list:
        black_listed.append((addr_num, addr_num+address_range-1))
    else:
        white_listed.append((addr_num, addr_num+address_range-1))

black_listed = sorted(black_listed)
white_listed = sorted(white_listed)

ip_ranges = []


def add_ips(left, right):
    if check_list(black_listed, left, right):
        if check_list(white_listed, left, right):
            if left == right:
                print(-1)
                exit()
            boundary = (right - left) // 2
            add_ips(left, left+boundary)
            add_ips(left+boundary+1, right)
        else:
            ip_ranges.append(number_to_address(left) + '/' + ranges[right-left+1])


def check_list(list_to_check, left, right):
    if list_to_check:
        le, ri = list_to_check[find_index(list_to_check, left)]
        if left <= le <= right or left <= ri <= right or le <= left <= ri or le <= right <= ri:
            return True
    return False


def find_index(list_to_check, index):
    left, right = 0, len(list_to_check) - 1
    while True:
        if left == right:
            return left
        mid = left + ((right - left) // 2)
        if list_to_check[mid][0] <= index <= list_to_check[mid][1]:
            return mid
        if list_to_check[mid][0] > index:
            right = mid
        else:
            left = mid+1


def number_to_address(number):
    addr_strs = []
    for mult in multiplication:
        left_mult = number // mult
        addr_strs.append(str(left_mult))
        number -= left_mult * mult
    return '.'.join(addr_strs)


add_ips(0, (2**32)-1)
print(len(ip_ranges))
print('\n'.join(ip_ranges))