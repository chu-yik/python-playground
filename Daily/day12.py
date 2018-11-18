'''
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

# space complexity?
# time complexity?

# start with recursion, end case will be n == 0, 1 or 2?

# assuming n >= 0
def waysToClimbSteps(n):
    if n == 0:
        return 1
    if n-1 >= 0:
        count = waysToClimbSteps(n-1)
    if n-2 >= 0:
        count += waysToClimbSteps(n-2)
    return count

'''
print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(0), 0))
print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(1), 1))
print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(2), 2))
print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(3), 3)) # 1,1,1 // 1,2 // 2,1
print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(4), 4))
print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(5), 5))
print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(6), 6))
print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(7), 7))
# print("there are {0} ways to climb {1} steps".format(waysToClimbSteps(34), 34)) # too slow
'''

# simple recursion with space complexity O(1), but time too slow
# O(n^2)

# CORRECTION!
# from readings the space is O(n) from call stack...
# and time it is somewhere around O(2^n) ... 1.618^n ??? :wtf:

# looks like fib number sequence, might want to do memo
def waysToClimbStepsWithMemo(n, lookup):
    if n == 0:
        return 1

    if n-1 >= 0:
        if lookup[n-1] is None:
            lookup[n-1] = waysToClimbStepsWithMemo(n-1, lookup)
        count = lookup[n-1]

    if n-2 >= 0:
        if lookup[n-2] is None:
            lookup[n-2] = waysToClimbStepsWithMemo(n-2, lookup)
        count += lookup[n-2]

    return count

# with lookup then Space Complexity becomes O(n)
# Time complexity is of the magnitude O(n) because all lookup needs to be filled at least once?

def testCode(n):    
    lookup = [None]*n
    ways = waysToClimbStepsWithMemo(n, lookup)
    print("lookup - there are {0} ways to climb {1} steps".format(ways, n))

testCode(0)
testCode(1)
testCode(2)
testCode(3)
testCode(4)
testCode(5)
testCode(6)
testCode(7)
testCode(33)

'''
now the fun part - how do i test the {1, 3, 5}? umm...
6 steps
1,1,1,1,1,1
1,1,1,3
1,1,3,1
1,3,1,1
1,5
3,1,1,1
3,3
5,1

= 8?
'''

def waysToClimbStepsWithMemoAndOption(n, lookup, stepOption):
    if n == 0:
        return 1

    count = 0
    for step in stepOption:
        target = n - step
        if target >= 0:
            if lookup[target] is None:
                lookup[target] = waysToClimbStepsWithMemoAndOption(target, lookup, stepOption)
            count += lookup[target]

    return count

def testStepOption(n, stepOption):
    lookup = [None]*n
    ways = waysToClimbStepsWithMemoAndOption(n, lookup, stepOption)
    print("option - there are {0} ways to climb {1} steps with options {2}".format(ways, n, stepOption))

options = set([1, 3, 5])
testStepOption(33, options)

# lesson leart:
# start with the simple answer and then refactor
# make it work, make it right, make it fast