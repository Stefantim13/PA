v = []
l = []
def citire():
    n = int(input())
    for i in range(0, n):
        x = int(input())
        v.append(x)
def afisare(a):
    for x in a:
        print(x, end = ' ')
def creeaza_lista():
    l = [x for x in v if x > 0]
    return l
if __name__ == "__main__":
    print("SALUT")