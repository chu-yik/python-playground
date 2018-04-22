# solution modified from
# https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/

def longest_consective(A, m):
	n = len(A)

	index_left = 0
	index_right = 0
	saved_left = 0
	saved_size = 0
	zero_count = 0

	while index_right < n:

		if zero_count <= m:
			if A[index_right] == 0:
				zero_count += 1
			index_right += 1

		if zero_count > m:
			if A[index_left] == 0:
				zero_count -= 1
			index_left += 1

		if index_right - index_left > saved_size:
			saved_size = index_right - index_left
			saved_left = index_left

	for i in range(saved_size):
		if A[saved_left + i] == 0:
			print(saved_left + i, end = " ")

	return saved_size

A = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
m = 2

print("Indexes of zeroes to be flipped are", end = " ")
max_length = longest_consective(A, m)
print("Maximum length is {0}".format(max_length))
