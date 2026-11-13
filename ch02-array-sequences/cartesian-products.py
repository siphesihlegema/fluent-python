colors = ["black", "white"]
sizes = ["L", "M", "S"]

# we can change order by swaping the for loops
pairs = [(color, size) for size in sizes
                       for color in colors]

print(pairs)

