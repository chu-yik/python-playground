'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
Implement an XOR linked list; 

it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer functions 
that converts between nodes and memory addresses.
'''

# ref: https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/
#
# take the following list as an example 
# A <> B <> C <> D
# pointer = prev XOR next 
# npx(A) = 000000 ^ add(B)
# npx(B) = add(A) ^ add(C)
# npx(C) = add(B) ^ add(D)
# npx(D) = add(C) ^ 000000

# 1 = 0 ^ 1
# 1 = 1 ^ 0
# 0 = 1 ^ 1
# 0 = 0 ^ 0
# so the idea is take any two and apply XOR we will get the third 

# to traverse the list we need to have the address of either prev or next node

class Node:
    def __init__(self, data, npx=None):
        self.data = data
        self.npx = npx

def add(element, head):
    element.npx = get_pointer(head) ^ head.npx
    
def get(index, head):
    if index < 1: # index 0 will be current, assume no negative index
        return head
    else
        next_ptr = get_pointer(head) ^ head.npx
        next_node = dereference_pointer(next_ptr)
        return get(index-1, next_node)
    

head = Node(A)
add(Node(B), head)
add(Node(C), head)
add(Node(D), head)

get(2, head).data # should be C