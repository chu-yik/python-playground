# collection.Count can be used to find
# the most common elements in an iterable

import collections

c = collections.Counter('helloworld')

print('c is {}'.format(c))

print('3 most common elements are: {}'.format(c.most_common(3)))
