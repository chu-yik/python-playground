# https://www.youtube.com/watch?v=qli-JCrSwuk

import time

def helper(data, k):
    if k is 0:
        return 1
    
    i = len(data) - k
    if data[i] is '0':
        return 0

    count = helper(data, k-1)

    if k >= 2 and int(data[i:i+2]) <= 26:
        count += helper(data, k-2)

    return count

def decode(s):
    return helper(s, len(s))

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