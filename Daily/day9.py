'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

'''
answer algorithm from
https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
'''

# incl = max sum including previous number
# excl = max sum excluding previous number
def largest_non_adjacent_sum(array):
    if len(array) is 0:
        return 0
    if len(array) is 1:
        return array[0]
    
    incl = 0
    excl = 0
    for x in array:
        # should skip if x not > 0?
        max_so_far = max(incl, excl)
        incl = x + excl
        excl = max_so_far

    return max(incl, excl)
    
print(largest_non_adjacent_sum([2, 4, 6, 2, 5]))
print(largest_non_adjacent_sum([5, 1, 1, 5]))
print(largest_non_adjacent_sum([-5, 5, 0, -1, -5]))
print(largest_non_adjacent_sum([5, 5, 10, 100, 10, 5]))
print(largest_non_adjacent_sum([5,  5, 10, 40, 50, 35]))
print(largest_non_adjacent_sum([5,  5, 10, -40, 0, 50, 35]))
print(largest_non_adjacent_sum([-5]))
print(largest_non_adjacent_sum([]))