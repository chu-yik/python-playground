'''
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
'''

def pop_n_to_queue_and_push(stack, n):
    queue = []
    for _ in range(n):
        queue.append(stack.pop())
    for _ in range(n):
        stack.append(queue.pop(0))
        

def interleave(stack):
    print('given stack: {0}'.format(stack))
    n = len(stack)
    # queue = []
    if n < 3:
        print('result stack: {0}'.format(stack))
    else:
        for x in range(n-1, 1, -1):
            pop_n_to_queue_and_push(stack, x)
        print('result stack: {0}'.format(stack))
    print('---')

interleave([1, 2, 3, 4, 5]) # [1, 5, 2, 4, 3]
interleave([1, 2, 3, 4]) # [1, 4, 2, 3]
interleave([1, 2, 3, 4, 5, 6]) # [1, 6, 2, 5, 3, 4]
interleave([1, 2, 3, 4, 5, 6, 7]) # [1, 7, 2, 6, 3, 5, 4]
interleave([])
interleave([1])
interleave([1, 2])
interleave([1, 2, 3]) # [1, 3, 2]
