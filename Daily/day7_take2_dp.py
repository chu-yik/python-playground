# https://www.youtube.com/watch?v=qli-JCrSwuk

'''
dynamic programming, or memorization is to help tackle the worst case scenario
decode(11111111...111)
where repeated calculation is needed
trade off between memory and time
'''
import time

def helper_dp(data, k, memo):
    if k is 0:
        return 1
    
    i = len(data) - k
    if data[i] is '0':
        return 0

    if memo[k] is not None:
        return memo[k]

    count = helper_dp(data, k-1, memo)

    if k >= 2 and int(data[i:i+2]) <= 26:
        count += helper_dp(data, k-2, memo)

    memo[k] = count
    return count

def decode(s):
    memo = [None] * (len(s)+1)
    return helper_dp(s, len(s), memo)

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