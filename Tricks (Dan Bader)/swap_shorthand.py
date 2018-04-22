def printab(a, b):
	print('a {0}, b {1}'.format(a, b))

a = 23
b = 45
printab(a, b)

# traditional swapping
tmp = a
a = b
b = tmp
printab(a, b)

# do this for shorthand swapping
a, b = b, a
printab(a, b)
