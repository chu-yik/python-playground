# pattern break down
# mod 16:
# 0-6  -> 1101100
# 8-14 -> 1100100
# anything that is exactly (2**n)-1 is always 1
# e.g. 0, 1, 3, 7, 15, 31

def break_down(num):
	pattern = [1,1,0,1,1,0,0,'x',1,1,0,0,1,0,0,'y']
	i = num % 16
	p = pattern[i]
	if p is 'x':
		x = num % 32
		if x == 7:
			print(1, end="")
		else:
			print(0, end="")
	elif p is 'y':
		break_down(num//16)
	else:
		print(p, end="")

for i in range(999, 1012):
	break_down(i)

# order = 10
# array = [0] * (2**order - 1)
# array[0] = 1

# current_order = 1
# while current_order < order:
#     pivot = 2**current_order - 1
#     array[pivot] = 1
#     for i in range(1, pivot):
#         array[pivot+i] = 1 - array[pivot-i]
#     current_order += 1

# for i in range(0, 2**order - 1):
#     print(array[i], end="")
#     if i is not 0 and (i+1) % 16 == 0:
#     	print("({0})\n".format(i//16 % 32), end = "")