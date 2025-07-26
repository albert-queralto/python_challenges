class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    def isMirror(left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    return isMirror(root, root)

if __name__ == "__main__":
    # Example 1
    # Input: root = [1,2,2,3,4,4,3]
    # Output: true
    # Explanation: The above binary tree is symmetric.
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(isSymmetric(root))
    
    # Example 2
    # Input: root = [1,2,2,null,3,null,3]
    # Output: false
    # Explanation: The above binary tree is not symmetric.
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    print(isSymmetric(root))
    
    # Example 3
    # Input: root = [1,2,2,2,2]
    # Output: true
    # Explanation: The above binary tree is symmetric.
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(2)
    root.right.right = TreeNode(2)
    print(isSymmetric(root))