n = int(input())
p = input()
p = p.split()
maxim = 0
p = [float(x) for x in p]
'''
for i in range(1, n):
    dif.append(p[i]-p[i-1])
'''
dif = [p[i] - p[i-1] for i in range(1,n)]
idx = dif.index(max(dif))
print(idx + 1, dif[idx])