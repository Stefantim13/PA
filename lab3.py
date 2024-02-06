


def ex1():
    fin = open("test.in", "r")
    fout = open("test.out", "w")
    
    grade = 1
    for line in fin.readlines():
        line = line.strip()

        x = int(line.split('*')[0])

        y, eq = line.split('*')[1].split('=')

        y = int(y)
        eq = int(eq)

        if(x * y == eq):
            grade += 1
            fout.write(f"{line} Corect\n")
        else:
            fout.write(f"{line} Gresit {x * y}\n")
    fout.write(f"Nota {grade}")

def ex2():
    fin = open("cheltuieli.txt")

    journal = "".join(fin.readlines())

    def is_float(x):
        return x.replace(".", "", 1).isnumeric()
    
    nums = [float(x) for x in journal.split() if is_float(x)]
    
    sum = 0
    for i in range(0, len(nums), 2):
        sum += nums[i] * nums[i + 1]
    print(sum)


def ex3():

    prop = "ana bana are pere prune ana pere prune ana ana ana".split()
    
    freq = {
        x:prop.count(x) for x in prop
    }
    

    freq_list = {
        f : [x for x in freq.keys() if freq[x] == f] for f in freq.values()
    }

    min_freq = min(freq_list.keys())
    max_freq = max(freq_list.keys())

    print(min(freq_list[min_freq]), min(freq_list[max_freq]))
     

def ex4():
    d1 = {
        'A': 1,
        'B': 2
    }

    d2 = {
        'B': 3,
        'C': 2
    }

    d = {
        x : d1.get(x, 0) + d2.get(x, 0) for x in d1.keys() | d2.keys()
    }

    print(d)


def ex5():
    prop = "Langa o cabana stand pe o banca un bacan a spus un banc bun".split()
    x = "bacan"

    ans = [y for y in prop if set(x) == set(y)]

    print(ans)


def ex6():
    l = [1, 2, 3, 4]
    ans = [(l[i], l[i + 1]) for i in range(len(l) - 1)]

    print(ans)

def ex7():
    n = 5
    l = [[f"{i}*{j + 1}={i * (j + 1)}" for j in range(n)] for i in range(n)]

    print(l)

def ex8():
    fin = open("test.in", "r")

    cuvinte = "".join(fin.readlines()).split()
    
    d = {x[-2:] : sorted([y for y in cuvinte if y.endswith(x[-2:])]) for x in cuvinte}
    # for x in cuvinte:
    #     d[x[-2:]] = []

    # for x in cuvinte:
    #     d[x[-2:]].append(x)

    # for x in d.keys():
    #     d[x].sort()
    print(d)       


def ex10():
    x = [123, 12, 25, 50, 100] #100 12 123 25 50
    x.sort(key = lambda x : str(x))
    print(x)

ex10()
