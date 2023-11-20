lstud = [("Popescu Ion", 135, (5, 7, 3, 0, 4)),("Popa Anca", 131, (5, 7, 3)),("Mihai Ana", 135, (7, 3, 3, 2, 4)),("Mihai Ana", 132, (7, 0, 3, 0)),("Ionescu Clara", 131, (5, 5, 3)),("Bobescu Iulia", 135, (5, 5, 5, 3, 3))]
def situatie_scolara(lista, credite):
    for i in range(len(lista)):
        if 0 not in lista[i][2] and sum(lista[i][2]) >= credite:
            lista[i] += (True,)
        else:
            lista[i] += (False,)
def c1(t):
    return t[1], t[0]
def c2(t):
    return -t[3],t[0]
def c3(t):
    return -sum(t[2]), t[1], t[0]
def c4(t):
    return t[1], -t[3], -sum(t[2]), t[0]
situatie_scolara(lstud, 15)
lstud.sort(key = c4)
print(*lstud, sep='\n')