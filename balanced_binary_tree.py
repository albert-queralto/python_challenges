class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(node):
    if not node:
        return 0
    return max(height(node.left), height(node.right)) + 1

def is_balanced(root):
    if not root:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) > 1:
        return False
    
    return is_balanced(root.left) and is_balanced(root.right)

# Example usage:
# Construct a binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(is_balanced(root))  # Output: True