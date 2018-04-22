# print playground - python 3.6
# https://docs.python.org/3.6/tutorial/inputoutput.html

import sys
import math

s = 'Hello World'
print(str(s))
print(repr(s))

# str.rjust()
# str.ljust()
# str.zfill()

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# keyword in argument
print('{guy} is {adjective}.'.format(
    guy='Fish Ball',
    adjective='absolutely stupid'))

print('The story of {1}, {0}, and {other}.'.format('Tom', 'Mary',
    other='Dick'))

# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:
contents = 'gold'
print('Fish ball\'s mind is full of {!r}.'.format(contents))

print('The value of PI is approximately {0:.3f}.'.format(math.pi))

print(sys.version)

print (3//2)
print (4//2)