def find_pair(A):
    print("given array: {0}".format(A))
    n = len(A)
    # first find existing number of paris
    current_pair = 0
    for i in range(n - 1):
        if (A[i] == A[i + 1]):
            current_pair = current_pair + 1
    # then compute which flip bring the most positive change
    best_change = -1
    for i in range(n):
        count = 0
        if (i > 0):
            if (A[i - 1] != A[i]):
                count = count + 1
            else:
                count = count - 1
        if (i < n - 1):
            if (A[i + 1] != A[i]):
                count = count + 1
            else:
                count = count - 1
        best_change = max(best_change, count)

    return current_pair + best_change

if __name__ == "__main__":
    print(find_pair([0]))
    print(find_pair([0, 1]))
    print(find_pair([0, 0]))
    print(find_pair([0, 0, 0]))
    print(find_pair([0, 0, 0, 0]))
    print(find_pair([0, 0, 1, 1]))
    print(find_pair([1, 0, 0, 0]))
    