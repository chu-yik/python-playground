# function arguement unpacking
def myfunc(x, y, z):
	print(x, y ,z)

myfunc(1, 2, 3)

my_tuple = (4, 5, 6)
myfunc(*my_tuple)

my_dict = {
	'y': 7,
	'x': 8,
	'z': 9,
}
# note that keys would have to match func signature
# cannot have more or less keys
myfunc(**my_dict)
