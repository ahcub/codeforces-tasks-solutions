n = int(input())
strings = [sorted(input()) for i in range(n)]

for string in strings:
    if len(string) != len(set(string)):
        print('No')
    else:
        prev = ord(string[0])
        for ch in string[1:]:
            new_ = ord(ch)
            if prev+1 != new_:
                print('No')
                break
            else:
                prev = new_
        else:
            print('Yes')

