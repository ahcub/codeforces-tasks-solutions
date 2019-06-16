from collections import defaultdict

n = int(input())
sound = 'aeoiu'
mapped_words = {}


for i in range(n):
    c = 0
    l = None
    word = input()
    for ch in word:
        if ch in sound:
            c += 1
            l = ch
    if c not in mapped_words:
        mapped_words[c] = defaultdict(list)
    mapped_words[c][l].append(word)

first_words = []
second_pairs = []
for reg in mapped_words.values():
    fw = []
    for let_v in reg.values():
        if (len(let_v) % 2) != 0:
            fw.append(let_v[-1])
            second_pairs.extend(zip(let_v[:len(let_v) // 2], let_v[len(let_v) // 2:-1]))
        else:
            second_pairs.extend(zip(let_v[:len(let_v) // 2], let_v[len(let_v) // 2:]))
    if len(fw) > 1:
        if (len(fw) % 2) == 1:
            first_words.extend(zip(fw[:len(fw) // 2], fw[len(fw) // 2:-1]))
        else:
            first_words.extend(zip(fw[:len(fw) // 2], fw[len(fw) // 2:]))

if len(first_words) < len(second_pairs):
    border = len(second_pairs) - ((len(second_pairs) + len(first_words)) // 2)
    first_words.extend(second_pairs[-border:])
    second_pairs = second_pairs[:-border]

pairs = list(zip(first_words, second_pairs))
print(len(pairs))
for (f1, f2), (s1, s2) in pairs:
    print(f1, s1)
    print(f2, s2)
