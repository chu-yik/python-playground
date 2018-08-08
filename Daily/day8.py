'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

# solution modified from
# https://webcache.googleusercontent.com/search?q=cache:Wm_eJwLNS8sJ:https://www.dailycodingproblem.com/blog/unival-trees/+&cd=1&hl=en&ct=clnk&gl=hk

# count from the leave

# return count, boolean (whether root is a universal tree)
def helper(root):
    if root is None:
        return 0, True
    left_count, is_left_universal = helper(root.left)
    right_count, is_right_universal = helper(root.right)
    total = left_count + right_count
    if is_left_universal and is_right_universal:
        if root.left is not None and root.right is not None and root.value == root.left.value and root.value == root.right.value:
            return total + 1, True
        if root.left is None and root.right is None:
            return total + 1, True
        return total, False
    return total, False

def count_universal(root):
    count, _ = helper(root)
    return count

# too lazy to write test case but this should work (famous last words lol)
