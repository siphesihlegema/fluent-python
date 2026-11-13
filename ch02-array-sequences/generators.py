x = ["black", "white"]
y = ["L", "M", "S"]

z = (shirt for shirt in (f'{c} {s}' for c in x for s in y))

for i in z:
    print(i)
