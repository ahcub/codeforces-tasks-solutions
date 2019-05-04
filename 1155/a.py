n = int(input())
s = input()

max_char_i = 0
max_char = s[0]
for i, c in enumerate(s[1:], 1):
    if c < max_char:
        print('YES')
        print(max_char_i+1, i+1)
        exit()
    max_char_i = i
    max_char = c
print('NO')