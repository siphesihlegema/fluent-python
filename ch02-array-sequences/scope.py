x = 'ABC'

codes = [ord(i) for i in x] # i is defined in the local scope of the list comprihension
print(codes)

codes = [last := ord(i) for i in x] # however if we assign a variable using the (Wolrus operator) it can acces global scope
print(last)



