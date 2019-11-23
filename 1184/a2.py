ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))


n = int(input())
sa = int(input(), 2)
ans = 0
for i in range(1, n):
    if sa == ror(i, i, n)
