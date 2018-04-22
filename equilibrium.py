import sys
import time

# assumption:
# length of array is an integer within the range [0..100,000]
# each element of array is an integer within the range [−2,147,483,648..2,147,483,647]

# O(n^2) solution, iterate through the index and check the sum for left 
# and right side of the pivot
def equilibrium(array):
	found = []
	for i in range(0, len(array)):
		left = sum(array[0:i])
		right = sum(array[i+1:])
		if left == right:
			found.append(i)
		# print("index {0}, left {1}, right {2}".format(i, left, right))
	return found

# O(n) solution, iterate through array while comparing left and right sum
# by subtracting an element from right side (pivot), compare, then move
# it to the left side (change pivot)
def better_equilibrium(array):
	found = []
	left = 0
	right = sum(array)
	for i in range(0, len(array)):
		right -= array[i]
		# print("index {0}, left {1}, right {2}".format(i, left, right))
		if left == right:
			found.append(i)
		left += array[i]
	return found

if __name__ == "__main__":

	print(sys.version)
	print("Maximum integer size: {0:,}".format(sys.maxsize))

	# array = [-1, 3, -4, 5, 1, -6, 2, 1]
	array = [-7, 1, 5, 2, -4, 3, 0]

	start_time = time.time()

	found = equilibrium(array)

	if len(found) == 0:
		print("no equilibrium found, -1")
	else:
		print("equilibrium index(es) are {0}".format(found))
	
	print("time used = %.10f seconds" % (time.time() - start_time))

	start_time = time.time()

	found = better_equilibrium(array)

	if len(found) == 0:
		print("no equilibrium found, -1")
	else:
		print("equilibrium index(es) are {0}".format(found))
	
	print("time used = {0:.10f} seconds".format(time.time() - start_time))