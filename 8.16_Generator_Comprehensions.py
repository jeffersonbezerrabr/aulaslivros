# Da mesma forma que podemos usar list comprehension, podemos criar geradores 
# apenas subistituindo os colchetes ([]) por parênteses.

print([x for x in range(10) if x % 3 == 0])

print(x for x in range(10) if x % 3 == 0)

for y in (x for x in range(10) if x % 3 == 0):
    print(y)