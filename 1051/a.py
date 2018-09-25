"""http://codeforces.com/problemset/problem/1051/A"""

from collections import defaultdict

t = []
for i in range(int(input())):
    t.append(input())

v_const = {
    'upper': 'A',
    'lower': 'a',
    'numbers': '1',
}

char_types = list(v_const.keys())

n_const = [str(i) for i in range(10)]
for p in t:
    indexes = defaultdict(list)

    for i, v in enumerate(p):
        if v in n_const:
            indexes['numbers'].append(i)
        elif v.islower():
            indexes['lower'].append(i)
        else:
            indexes['upper'].append(i)

    missing_arrays = {key: None for key in char_types if key not in indexes}
    keys = list(missing_arrays.keys())
    if len(keys) == 0:
        print(p)
    elif len(keys) == 1:
        for key, val in indexes.items():
            if len(val) > 1:
                missing_arrays[keys[0]] = val[0]
                break
        n_p = list(p)
        n_p[missing_arrays[keys[0]]] = v_const[keys[0]]
        print(''.join(n_p))
    else:
        n_p = list(p)
        n_p[0] = v_const[keys[0]]
        n_p[1] = v_const[keys[1]]
        print(''.join(n_p))
