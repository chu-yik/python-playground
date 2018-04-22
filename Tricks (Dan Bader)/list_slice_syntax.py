# using python list slice syntax WITHOUT indices:

# 1. clear all elements from a list
list = [1, 2, 3, 4, 5]
print('list is {}'.format(list))
del list[:]
print('after del list[:] - {}'.format(list))

# 2. replace all elements of a list without creating a new list object
a = list
list[:] = [7, 8, 9] 
# if list = [7, 8, 9] then the result is different
# list = [7, 8, 9]
print('a: {}'.format(a))
print('list: {}'.format(list))
print('a is list: {}'.format(a is list))

# 3. create shallow copy of a list
b = list[:]
print('b: {}'.format(b))
print('b is list: {}'.format(b is list))

# MC: so list is the pointer to object
# list[:] is the content of the object
