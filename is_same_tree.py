class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # If both trees are empty, they are the same
    if not p and not q:
        return True
    # If one tree is empty and the other is not, they are not the same
    if not p or not q:
        return False
    # If the values of the current nodes are different, they are not the same
    if p.val != q.val:
        return False
    # Recursively check the left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

if __name__ == "__main__":
    # Example 1
    # Construct the trees
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    
    # Output: True
    print(isSameTree(p, q))
    
    # Example 2
    # Construct the trees
    p = TreeNode(1)
    p.left = TreeNode(2)
    
    q = TreeNode(1)
    q.right = TreeNode(2)
    
    # Output: False
    print(isSameTree(p, q))
    
    # Example 3
    # Construct the trees
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    
    # Output: False
    print(isSameTree(p, q))