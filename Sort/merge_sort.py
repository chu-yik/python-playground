'''
https://www.geeksforgeeks.org/merge-sort/
'''

def merge_sort(array):
    if array is None:
        return None
    size = len(array)
    if size > 1:
        mid = int(size / 2)
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        
        temp = []
        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                temp.append(left[left_index])
                left_index += 1
            else:
                temp.append(right[right_index])
                right_index += 1
        
        if left_index < len(left):
            temp.extend(left[left_index:])
        if right_index < len(right):
            temp.extend(right[right_index:])

        return temp
    return array

print(merge_sort(None))                                 # None
print(merge_sort([]))                                   # []
print(merge_sort([0]))                                  # [0]
print(merge_sort([1, 1, 1, 1]))                         # [1, 1, 1, 1]
print(merge_sort([-1, -1, -1]))                         # [-1, -1, -1]
print(merge_sort([12, 12, 23, 4 , 6, 6, 10, -35, 28]))  # [-35, 4, 6, 6, 10, 12, 12, 23, 28]
print(merge_sort([12, 15, -23, -4 , 6, 10, -35, 28]))   # [-35, -23, -4, 6, 10, 12, 15, 28]
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))           # [3, 9, 10, 27, 38, 43, 82]
print(merge_sort([4, 6, 10, 12, 15, 23, 28, 35]))       # [4, 6, 10, 12, 15, 23, 28, 35]
