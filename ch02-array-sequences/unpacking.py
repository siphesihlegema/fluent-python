a, b, *rest = range(10)
print(a, b, rest)

def func(a, b, c, d, *rest):
    return a, b, c, rest

x = func(*[1, 2], 3, *range(4, 7))
print(x)
