def gen_f(k):
    def f(x):
        return x < k
    return f