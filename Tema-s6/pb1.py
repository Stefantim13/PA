import random

def generare_matrice(n, m):
    s = random.sample(range(0,100), n * m)
    s.sort()
    M = [s[i * m: (i+1) * m]  for i in range(n)]
    return M
def afisare(M):
    for i in range(n):
        for j in range(m):
            print(M[i][j], end = " ")
        print("\n")

def cautare(n, m, x, M):
    def liniar(): # complexitate n * m
        for i in range(n):
            for j in range(m):
                if(M[i][j] == x):
                    return(i, j)
        return None
    def cautare_binara():
        for i in range(n):
            st = 0
            dr = m - 1
            while st <= dr:
                mij = int((st + dr) / 2)
                if M[i][mij] < x:
                    st = mij + 1
                else:
                    dr = mij - 1
            if st < m and M[i][st] == x:
                return(i,st)
        return None
    
    def lee():
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if M[i][j] == x:
                return (i,j)
            elif M[i][j] < x:
                i += 1
            else:
                j -= 1
        return None
            
    return liniar(), cautare_binara(), lee()
    
n = int(input())
m = int(input())

M = generare_matrice(n, m)
afisare(M)
x = int(input())


a, b, c = cautare(n, m, x, M)

print(f"Cautare liniara: {a}")
print(f"Cautare binara: {b}")
print(f"Lee: {c}")
