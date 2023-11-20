L = ["zi", "ana", "sac", "acadea", "bac", "nori", "zar", "mi", "abur"]
#a)
A = L
A.sort(reverse = True)
print(A)
#b)
B = L
B.sort(key = lambda x: (len(x),x))
print(B)
#c)
C = L
C.sort(key = lambda x : len(x))
print(C)
