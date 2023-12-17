f = open("date.in")

def rezolva(x1,y1,x2,y2,c):
    global q
    global v
    if x2 - x1 == 1:
        if (a == x1 or a == x2) and (b == y1 or b == y2):
            v[x1][y1] = v[x1][y2] = v[x2][y1] = v[x2][y2] = q + 1
            v[a][b] = 0
        else:
            v[x1][y1] = v[x1][y2] = v[x2][y1] = v[x2][y2] = q + 1
            if c == 0:
                v[x2][y2] = int(q / 4) * 4 + 5
            elif c == 1:
                v[x1][y2] = int(q / 4) * 4 + 5
            elif c == 2:
                v[x2][y1] = int(q / 4) * 4 + 5
            else:
                v[x1][y1] = int(q / 4) * 4 + 5
        q += 1
    else:
        rezolva(x1,y1,int((x1 + x2 - 1) / 2) ,int((y1 + y2 - 1) / 2), 0)
        rezolva(int((x1 + x2 + 1) / 2), y1, x2, int((y1 + y2 - 1) / 2), 1)
        rezolva(x1, int((y1 + y2 + 1) / 2), int((x1 + x2 - 1) / 2), y2, 2)
        rezolva(int((x1 + x2 + 1) / 2), int((y1 + y2 + 1) / 2), x2, y2, 3)


q = 0
l = f.readlines()
n = int(l[0])
k = l[1].split()
a = int(k[0])
b = int(k[1])
v = [[]]
n = 1 << n

v = [[0 for i in range(n + 2)] for j in range(n + 2)]
rezolva(1,1, n, n, 1)
for i in range(1,n + 1):
    for j in range(1, n + 1):
        print(v[i][j],end=' ')
    print("")