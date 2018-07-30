# This problem was asked by Stripe.
# 
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# 
# You can modify the input array in-place.

# solution ideas from
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
#
# brute force search array for +ve number from 1    - O(n^2) time
# sort array and then scan                          - O(n-log-n + n) time
# build hash table for positive integers            - O(n) time, O(n) space
# remove 0 and negative numbers, index trick        - O(n) time, O(1) space

# array should contain only +ve numbers, i.e. no 0, no -ve
# use array index as indicators:
# traverse the array
# if positive number seen
# check if index = number-1 is < array.length, if so
#   mark the element in that number-1 index negative
# when done, find the first index that the content is non-negative
#   index+1 will be the answer
# otherwise array.length+1 will be answer

def remove_zero_and_negative_from(array):
    for i, x in reversed(list(enumerate(array))):
        if x < 1:
            del array[i]

def index_trick(array):
    for x in array:
        index = abs(x)-1
        if index < len(array) and array[index] > 0:
            array[index] = -array[index]

def find_missing_positive(array):
    print("given array: {0}".format(array))
    remove_zero_and_negative_from(array)
    index_trick(array)
    answer = len(array)+1
    for i, x in enumerate(array):
        if x > 0:
            answer = i+1
            break
    print("answer: {0}".format(answer))
    

find_missing_positive([3, 4, -1, 1, -10, -11, 7, 0, -2])
find_missing_positive([1, 2, 0, 5, 8, 100, 1, 5, 8, 3])
find_missing_positive([1, 1, 1])
find_missing_positive([1])
find_missing_positive([])