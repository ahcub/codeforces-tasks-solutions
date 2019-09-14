n = int(input())
s = input()
t = input()
m = {
    ('aa', 'aa'): 'abc',
    ('bb', 'bb'): 'abc',
    ('cc', 'cc'): 'abc',
    ('ab', 'ab'): 'acb',
    ('ab', 'ab'): 'acb',
    ('ba', 'ba'): 'abc',
    ('ca', 'ca'): 'cba',
    ('cb', 'cb'): 'abc',
    ('ac', 'ac'): 'abc',
    ('bc', 'bc'): 'acb',
    ('aa', 'ab'): 'acb',
    ('aa', 'ac'): 'abc',
    ('aa', 'ba'): 'abc',
    ('aa', 'bb'): 'acb',
    ('aa', 'bc'): 'acb',
    ('aa', 'ca'): 'acb',
    ('aa', 'cb'): 'abc',
    ('aa', 'cc'): 'abc',
    ('ab', 'ac'): ('bc', 'a'),
    ('ab', 'ba'): ('bc', 'a'),
    ('ab', 'bb'): ('bc', 'a'),
    ('ab', 'bc'): 'cba',
    ('ab', 'ca'): 'cba',
    ('ab', 'cb'): ('b', 'ca'),
    ('ab', 'cc'): 'cba',
    ('ac', 'ba'): 'cab',
    ('ac', 'bb'): 'cab',
    ('ac', 'bc'): ('c', 'ba'),
    ('ac', 'ca'): ('c', 'ba'),
    ('ac', 'cb'): ('c', 'ab'),
    ('ac', 'cc'): 'abc',
    ('ba', 'bb'): 'abc',
    ('ba', 'bc'): ('ac', 'b'),
    ('ba', 'ca'): ('a', 'bc'),
    ('ba', 'cb'): 'bca',
    ('ba', 'cc'): 'bca',
    ('bb', 'bc'): 'acb',
    ('bb', 'ca'): 'acb',
    ('bb', 'cb'): 'abc',
    ('bb', 'cc'): 'abc',
    ('bc', 'ca'): ('ba', 'c'),
    ('bc', 'cb'): 'bac',
    ('bc', 'cc'): 'bac',
    ('ca', 'cb'): ('ab', 'c'),
    ('ca', 'cc'): 'acb',
    ('cb', 'cc'): 'abc',
}

r = m[(s, t)] if (s, t) in m else m[(t, s)]
if len(r) == 2:
    ans = r[0] * n + r[1] * n
else:
    ans = r * n
print('YES')
print(ans)
