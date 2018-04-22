import time

def count_subset_sum(numbers, index, target, lookup):

    if target == 0:
        return 1

    if index == 0:
        return 0

    if (index, target) not in lookup:

        next_index = index - 1
        next_number = numbers[next_index]
        count = count_subset_sum(numbers, next_index, target, lookup)

        if next_number <= target:
            count += count_subset_sum(numbers, next_index, target - next_number, lookup)

        lookup[(index, target)] = count

    return lookup[(index, target)]

def memo_sum(numbers, index, target, subset, memo):

    if target == 0:
        return 1
    if index == 0:
        return 0

    if (index, target) not in memo:
        count = memo_sum(numbers, index-1, target, subset, memo)
        if numbers[index-1] <= target:
            count += memo_sum(numbers, index-1, target - numbers[index-1], subset + [numbers[index-1]], memo)
        memo[(index, target)] = count

    return memo[(index, target)]


if __name__ == "__main__":

    start_time = time.time()

    target = 500

    # memo = dict()
    # total = memo_sum(numbers, len(numbers), target, [], memo)
    # print(total)
    # print("time used = %s seconds" % (time.time() - start_time))
    # start_time = time.time()

    lookup = dict()
    total = count_subset_sum(range(1,target), target-1, target, lookup)
    print(total)

    print("time used = %s seconds" % (time.time() - start_time))

