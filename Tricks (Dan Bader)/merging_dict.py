x = {
	'a': 1,
	'b': 2
}
y = {
	'b': 3,
	'c': 4
}

z = {**x, **y} # key in RHS overwrite dups in LHS
print("z is {0}".format(z))

# w = {**y, **x, **z}
w = {**y, **x}
print("w is {0}, b is differenct".format(w))
