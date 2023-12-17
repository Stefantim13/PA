import random
f = open("rucsac.in")
w = 0
def recursiv(v, w):
    st = []
    dr = []
    x = random.randint(0,len(v) - 1)
    ret = w
    for i in range(0, len(v)):
        if x == i:
            continue
        elif 1.0 * v[x][1] / v[x][0] <= 1.0 * v[i][1] / v[i][0]:
            ret += v[i][0]
            st.append(v[i])
        else:
            dr.append(v[i])
    if ret <= g and v[x][0] + ret > g:
        print(st)
        if ret != g:
            print(f"Numa o parte {v[x]} mai precis {g-ret} kg")
        return
    elif ret < g:
        if v[x][0] + ret < g:
            st.append(v[x])
            ret += v[x][0]
        print(st)
        recursiv(dr, ret)
    else:
        recursiv(st, w)
    
    

l = f.readlines()
g = int(l[0])
l = l[1:]
o = [[int(x) for x in y.split()] for y in l]
recursiv(o, 0)
#print(o)