# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

from functools import reduce

def product_array(array):
    # NOTE: array cannot be empty
    return reduce(lambda x, y: x * y, array) if len(array) is not 0 else 0

def product_array_except(array, index):
    return product_array(
        [x for i, x in enumerate(array) if i != index]
    )

# ---

def create_new_array(current_array):
    if len(current_array) < 2:
        return current_array

    new_array = []
    product = product_array(current_array)
    for i, x in enumerate(current_array): 
        new_array.append(
            int(product / x) if x is not 0 else product_array_except(current_array, i)
        )
    return new_array

def create_new_array_no_div(current_array):
    new_array = []
    for i in range(len(current_array)):
        new_array.append(
            product_array_except(current_array, i)
        )
    return new_array

def test_with(array):
    print("{0} -> {1}".format(
        array,
        create_new_array(array)
    ))
    print("{0} -> {1}".format(
        array,
        create_new_array_no_div(array)
    ))

test_with([1, 2, 3, 4, 5])
test_with([])
test_with([3, 2, 1])
test_with([1, 0, 1, -1]) # will error if use div without care
test_with([123, 1])
test_with([-1]) # need better definition for array with length 1
test_with([-3, -2, 1])