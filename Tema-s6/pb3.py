r = open("autostrada.in", "r")
w = open("autostrada.out", "w")
l = r.readlines()
length = int(l[0])
l = l[1:]
o = [[int(x) for x in y.split()] for y in l]
o.sort()
sol1 = []
sol1.append(o[0])
sum = 0
for a in o:
    if a[0] <= sol1[-1][1]:
        if sol1[-1][1] < a[1]:
            sol1[-1][1] = a[1]
    else:
        sol1.append(a)
for a in sol1:
    sum += a[1] - a[0]
    w.write(str(a))
    w.write("\n")

st = 0
sol2 = []
for a in sol1:
    sol2.append([st,a[0]])
    st = a[1]
sol2.append([sol1[-1][1],length])

w.write("\n")
for a in sol2:
    w.write(str(a))
    w.write("\n")

w.write("\n")

w.write(str(int(sum / length * 100))  + "%")

