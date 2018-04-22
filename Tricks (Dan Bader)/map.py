# this is an example from timeit.py
print("-".join(map(str, range(10))))

# printing the map object
obj = map(str, range(10))
print(obj)
# converting the map object to a list for printing
print(list(obj))

# --
# using lambda to map the given items

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

# --
# mapping with list of funcs

def original(x):
	return x
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [original, multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
    