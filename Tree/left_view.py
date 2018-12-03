class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def testTree1():
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5)
    root.right.right = Node(6)
    return root

def testTree2():
    root = Node(4) 
    root.left = Node(5) 
    root.right = Node(2) 
    root.right.left = Node(3) 
    root.right.right = Node(1)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    return root

def testTree3():
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    return root

'''
#1 -> BFS style
'''

# resursively getting tree height
def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

def allDataFromLevel(node, level):
    if node is None:
        return []
    if level is 0:
        return [node.data]
    elif level > 0:
        leftData = allDataFromLevel(node.left, level-1)
        rightData = allDataFromLevel(node.right, level-1)
        return leftData + rightData

def printLeftMostData(node, level):
    data = allDataFromLevel(node, level)
    print(data[0])
            
def leftView(root):
    h = height(root)
    for i in range(h):
        printLeftMostData(root, i)

root1 = testTree1()
leftView(root1)
print('--')
root2 = testTree2()
leftView(root2)
print('--')
root3 = testTree3()
leftView(root3)