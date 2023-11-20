def negative_pozitive(L):
    #return [x for x in L if x < 0],[x for x in L if x > 0]
    return list(filter(lambda x: x < 0, L)), list(filter(lambda x: x > 0, L))
a = [1,2,3,4,5,-1,2,-3,-4,-7, -2]

print(negative_pozitive(a))