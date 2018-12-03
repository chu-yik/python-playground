'''
ref: https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal_in_c.htm
'''
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

array = [27, 14, 35, 10, 19, 31, 42]

def insert(v, node):
    if v < node.data:
        if node.left is None:
            node.left = Node(v)
        else:
            insert(v, node.left)
    else:
        if node.right is None:
            node.right = Node(v)
        else:
            insert(v, node.right)


def createBinaryTree(array):
    root = None
    for v in array:
        if root is None:
            root = Node(v)
        else:
            insert(v, root)
    return root

# root = Node("A")
# left = Node("B")
# left.left = Node("D")
# left.right = Node("E")
# right = Node("C")
# right.left = Node("F")
# right.right = Node("G")
# root.left = left
# root.right = right

root = createBinaryTree(array)

def in_order_traversal(root):
    if root.left is not None:
        in_order_traversal(root.left)
    print("{} -> ".format(root.data), end="")
    if root.right is not None:
        in_order_traversal(root.right)

def pre_order_traversal(root):
    print("{} -> ".format(root.data), end="")
    if root.left is not None:
        pre_order_traversal(root.left)
    if root.right is not None:
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root.left is not None:
        post_order_traversal(root.left)
    if root.right is not None:
        post_order_traversal(root.right)
    print("{} -> ".format(root.data), end="")
    
print("\n--- in order traversal ---")
in_order_traversal(root)

print("\n--- pre order traversal ---")
pre_order_traversal(root)

print("\n--- post order traversal ---")
post_order_traversal(root)
