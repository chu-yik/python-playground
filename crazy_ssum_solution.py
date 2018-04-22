import numpy as np
import time

def solution1(n):
    dp = np.zeros((n+2,n+2))

    for i in range(n+1):
        dp[0,i] = 1

    for i in range(1,n+1):
        sm = 0
        for j in range(i, 0, -1):
            sm += dp[i-j,j+1]
            dp[i,j] = sm

    return int(dp[n,1])

def solution2(n):
    div=dict()
    a=dict()
    for i in range(1,n+1):
        s=0
        for j in range(1,i+1,2):
            if i%j==0:
                s+=j
        div[i]=s
        a[i]=(sum(a[i-j]*div[j] for j in range(1,i))+s)//i # A000009

    return(a[n]-1)

if __name__ == "__main__":

    n = 700

    start_time = time.time()
    s1 = solution1(n)
    print(s1)

    print("S1 time used = %s seconds" % (time.time() - start_time))

    start_time = time.time()
    s2 = solution2(n)
    print(s2)

    print("S2 time used = %s seconds" % (time.time() - start_time))


