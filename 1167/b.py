input_numbers = []
print('? 1 2', '? 2 3', '? 4 5', '? 5 6', sep='\n', flush=True)
input_numbers.append(int(input()))
input_numbers.append(int(input()))
input_numbers.append(int(input()))
input_numbers.append(int(input()))
numbers = {32: (4, 8), 60: (4, 15), 64: (4, 16), 92: (4, 23), 168: (4, 42), 120: (8, 15),
           128: (8, 16), 184: (8, 23), 336: (8, 42), 240: (15, 16), 345: (15, 23),
           630: (15, 42), 368: (16, 23), 672: (16, 42), 966: (23, 42)}

res = []
f = numbers[input_numbers[0]]
s = numbers[input_numbers[1]]
if f[0] == s[0]:
    res.extend([f[1], f[0], s[1]])
elif f[1] == s[0]:
    res.extend([f[0], f[1], s[1]])
elif f[1] == s[1]:
    res.extend([f[0], f[1], s[0]])
else:
    res.extend([f[1], f[0], s[0]])
f = numbers[input_numbers[2]]
s = numbers[input_numbers[3]]
if f[0] == s[0]:
    res.extend([f[1], f[0], s[1]])
elif f[1] == s[0]:
    res.extend([f[0], f[1], s[1]])
elif f[1] == s[1]:
    res.extend([f[0], f[1], s[0]])
else:
    res.extend([f[1], f[0], s[0]])

print('! ' + ' '.join([str(el) for el in res]))
