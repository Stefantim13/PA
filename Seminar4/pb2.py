def cauta(x, *liste):
    rez = []
    for list in liste:
        if x in list:
            rez.append(list)
    return rez

def genereaza(x, *liste):
    rez = []
    for list in liste:
        if x in list:
            yield list

x = int(input())
#print(cauta(x, [5, 1, 7, 3, 7], [2, 3], [-3, 7, 1]))

r = genereaza(x, [5, 1, 7, 3, 7], [2, 3], [-3, 7, 1])
print(next(r))
print(next(r))