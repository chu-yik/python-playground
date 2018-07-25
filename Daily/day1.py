# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
import time

def brute_force(list, k):
    for index, num in enumerate(list):
        for counter in list[index+1:len(list)]:
            # print("evaluating {0} + {1}".format(num, counter))
            if num + counter == k:
                return True
    return False

def add_up(list, k):
    counter_parts = []
    for i in list:
        if i in counter_parts:
            # print("found {0} in counter parts".format(i))
            return True
        else:
            counter = k - i
            # print("adding {0} to counter parts".format(counter))
            counter_parts.append(counter)
    # print("add up not found, counter_parts : {0}".format(counter_parts))
    return False
    
def time_function(func, run, list, k):
    start = time.time()
    for _ in range(run):
        func(list = list, k = k)
    end = time.time()
    # print("{0} - time: {1:.4f}s".format(func.__name__, end - start))
    return end - start

run = 1000
list = [10, 15, 3, 7, 9, 2, -9]
for k in range(-10, 25):
    brute_result = brute_force(list, k)
    add_result = add_up(list, k)
    if brute_result != add_result:
        print("WARNING: result mismatch, k {0}".format(k))
        break
    brute_time = time_function(brute_force, 1000, list, k)
    add_time = time_function(add_up, 1000, list, k)
    # print("K: {0} - brute > add - {1:.4f}s".format(
    #     k,
    #     brute_time - add_time
    # ))
    # if add_time > brute_time:
        # print("K: {0} - brute_force is faster? result: {1}".format(k, brute_result))
    
