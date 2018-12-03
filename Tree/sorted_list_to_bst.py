'''
'''

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# array = [1, 2, 3, 4, 5, 6, 7]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def to_bst(array):
    size = len(array)
    if size is 0:
        return None
    mid = int(size / 2)
    root = Node(array[mid])
    root.left = to_bst(array[:mid])
    root.right = to_bst(array[mid+1:])
    return root

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)

'''
BFS / level-order-traversal
'''

def get_height(node):
    if node is None:
        return 0
    lHeight = get_height(node.left)
    rHeight = get_height(node.right)
    if lHeight > rHeight:
        return lHeight + 1
    else:
        return rHeight + 1

def valuesInLevel(node, level):
    if node is None:
        return []
    if level is 0:
        return [node.data]
    elif level > 0:
        return valuesInLevel(node.left, level-1) + valuesInLevel(node.right, level-1)
    

def bfs(node):
    h = get_height(node)
    for i in range(h):
        print(valuesInLevel(node, i))

root = to_bst(array)
# in_order_traversal(root)
bfs(root)
