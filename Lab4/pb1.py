import math
'''
a = int(input())
b = int(input())
c = math.sqrt(a**2 + b**2)
print(c)
'''
b = int(input())
for a in range(b, 0, -1):
    c = math.sqrt(a**2 + b**2)
    if c == int(c):
        print(f'{a} {b} {int(c)}')