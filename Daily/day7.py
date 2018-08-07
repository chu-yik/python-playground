'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

import time

def decode(s):
    if len(s) is 0:
        return 1
    
    if s[0] is '0':
        return 0
    
    count = decode(s[1:])

    if len(s) > 1 and int(s[:2]) < 27:
        count += decode(s[2:])

    return count

print(decode('1')) # a
print(decode('11')) # aa or k
print(decode('111')) # ak, ka, or aaa
print(decode('123')) # abc, aw or lc
print(decode('163')) # afc, pc
print(decode('103')) # jc
print(decode('12311231623'))
start = time.time()
print(decode('1111111111111111111111111'))
end = time.time()
print('time used: {0:.4f}s'.format(end-start))