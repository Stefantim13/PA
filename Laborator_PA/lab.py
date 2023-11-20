'''s = 'ANA ARE MERE'
s.replace(s[0],'')
s.split(s[0])
print(s)'''

'''
s = "ana are {n} mere si {p} prune"
print(s.format(p = 5, n = 7))
'''
'''
PB 3 - var 1
t = 'abc'
s = 'abccabcababcc'
p = s.find(t)
while(p != -1):
    print(p, end = ' ')
    p = s.find(t, p + len(t))
'''
'''
t = 'abc'
s = 'abccabcababcc'
p = -1
try:
    p = s.index(t)
except: pass
'''
'''
while(p != -1):
    print(p, end = ' ')
    q = -1
    try:
        q = s.index(t, p + len(t))
    except: pass
    p = q
'''
'''
Pb 4
s = 'algoritm'
print(s.center(10))
while len(s) > 0:
    s = s[1:-1]
    print(s.center(10))
'''
'''
p = 'ana ana'
p = ' ' + p + ' '
t = 'ana'
t = ' ' + t + ' '
r = 'maria'
r = ' ' + r + ' '
p = p.replace(t, r)
p = p[1:-1]
print(p)
'''
'''
s = '1G10o4l'
l = [c for c in s if c.isalpha()]
for x in s:
    if x.isalpha():
        s = s.replace(x, '*')
s = s.split('*')
s = [int(x) for x in s if x.isnumeric()]
s = ''.join([l[i] * s[i] for i in range(len(l))])
print(s)
'''
p = 'GGGooooolllGG'
a = []
while len(s) != 0:
    a += f"{len(s) - len(s.strip(s[0]))}{s[0]}"
    s = s.lstrip(s[0])
print(a)