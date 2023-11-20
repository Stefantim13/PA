def matrice(n):
    M = [[0] * (n-1) + [1] for i in range(n - 1)]
    M.append([1] * n)
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            M[i][j] = M[i+1][j] + M[i][j+1]
    return M
def afisare(M):
    ncmax = max([len(str(max(linie))) for linie in M])
    for linie in M:
        for elem in linie:
            print(str(elem).rjust(ncmax), end = ' ')
        print()
n = int(input())
afisare(matrice(n))
