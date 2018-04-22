# the syntax :
#
# vals = [express
#         for value in collection
#         if condition]
#
# is the same as:
#
# vals = []
# for value in collection:
#   if condition:
#       vals.append(expression) 

even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)

# is equivalent to:
even_squares_2 = []
for x in range(10):
    if not x % 2:
        even_squares_2.append(x * x)
print(even_squares_2)
