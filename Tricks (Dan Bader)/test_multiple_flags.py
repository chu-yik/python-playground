x, y, z = 0, 2, 0 # change me

if x == 1 or y == 1 or z == 1:
	print("or condition")

if 1 in (x, y, z):
	print("1 in (x, y, z)")

# following only test for truthiness (not 0 is true)

if x or y or z: 
	print("x or y or z")

if any((x, y, z)):
	print("any((x, y, z))")
	