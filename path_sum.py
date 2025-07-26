class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    def dfs(node, currentSum):
        if not node:
            return False
        currentSum += node.val
        if not node.left and not node.right:  # Check if it's a leaf node
            return currentSum == targetSum
        return dfs(node.left, currentSum) or dfs(node.right, currentSum)
    
    return dfs(root, 0)

if __name__ == "__main__":
    # Example 1
    # Tree structure:
    #     5
    #    / \
    #   4   8
    #  /   / \
    # 11  13  4
    # /  \      \
    # 7   2      1
    #
    
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    
    targetSum = 22
    print(hasPathSum(root, targetSum))  # Output: True
    
    # Example 2
    # Tree structure:
    #     1
    #    / \
    #   2   3
    #
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    targetSum = 5
    print(hasPathSum(root, targetSum))  # Output: False
    
    # Example 3
    # Tree structure:
    #     1
    #
    
    root = TreeNode(1)
    
    targetSum = 0
    print(hasPathSum(root, targetSum))  # Output: False