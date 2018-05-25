# lambda keyword in Python provides a
# shortcut for declaring small and 
# anonymous functions:

add = lambda x, y: x + y
print(add(5, 3))

# lambdas are *function expressions*:
print((lambda x, y: x + y)(5, 3))

# NOTES
# they are not necessarily bound to a name (they can be anonymous)
# they can't use regular Python statements 
# they always include an implicit `return` statement.
