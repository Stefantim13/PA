def gcd(a, b):
    while(b):
        r = a % b
        a = b
        b = r
    return a
a = int(input())
b = int(input())
g = gcd(a,b)
print(g,a / g * b / g)
        