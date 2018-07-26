# This problem was asked by Google.
# 
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# 
# For example, given the following Node class
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# The following test should pass:
# 
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# thought process
# serialize into something like (root,(left),(right))
# edge cases
# only root -> (root)
# root and left -> ((root),(left),())
# root and right -> ((root),(),(right))
# root and both -> ((root),(left),(right))

def find_balance(s):
    for i, c in enumerate(s):
        if c is "," and s[:i].count("(") == s[:i].count(")"):
            return i
    return -1

def serialize(root):
    if root is None:
        return ""
    return "({0},{1},{2})".format(
        root.val,
        serialize(root.left),
        serialize(root.right),
    )

def deserialize(s):
    if len(s) is 0:
        return None

    if s[0] is "(" and s[-1] is ")":
        inside = s[1:-1]
        # print(inside)
        index = inside.find(',')
        if index is not -1:
            root_val = inside[:index]
            # print("root: {0}".format(root_val))
            left_and_right = inside[index+1:]
            # print(left_and_right)
            balance = find_balance(left_and_right)
            if balance is not -1:
                left = left_and_right[:balance]
                right = left_and_right[balance+1:]
                # print("left: {0}".format(left))
                # print("right: {0}".format(right))
                return Node(root_val, deserialize(left), deserialize(right))
    else:
        print("error in given string")

root = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right',None,Node('right.right')))
serialized = serialize(root)
print(serialized)
print(serialize(deserialize(serialized)))

