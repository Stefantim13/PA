import random

def generare_matrice():
    n = int(input())
    m = int(input())
    s = random.sample(range(0,100), n * m)
    s.sort()
    M = [s[i * m: (i+1) * m]  for i in range(n)]
def afisare()
    for i in range(n):
        for j in range(m):
            print(M[i][j], end = " ")
        print("\n")

def cautare(x)
    def liniar() # complexitate n * m
        for i in range(n):
            for j in range(m):
                if(M[i][j] == x):
                    return(i, j)
        return None
    def cautare_binara()
        for i in range(n)
            




generare_matrice()
afisare()
