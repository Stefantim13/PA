import math
def is_prime(a):
    ok = 1
    for j in range(2, math.ceil(math.sqrt(a + 1))):
        if a % j == 0:
            ok = 0
    return ok
def primes():  
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1

n = int(input())
g = primes()
for i in range(0, n):
    print(next(g))