n = int(input())
v = input()
v = v.split()
v = [int(x) for x in v]
for i in range(0,n-1,2):
    if v[i] > v[i+1]:
        v[i] = v[i] ^ v[i + 1]
        v[i+1] = v[i] ^ v[i + 1]
        

maxim = 0
minim = 1e9
for i in range(0, n-1, 2):
    if(maxim < v[i + 1]):
        maxim = v[i + 1]
    if(minim > v[i]):
        minim = v[i]
print(minim, maxim)