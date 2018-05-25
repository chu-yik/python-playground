# __repr__ vs. __str__

import datetime
today = datetime.date.today()

print('today is {}'.format(today))

# result of __str__ should be readable:
print('str: {}'.format(str(today)))

# result of __repr__ should be unambiguous:
print('repr: {}'.format(repr(today)))
