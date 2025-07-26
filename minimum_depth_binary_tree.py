from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque([(root, 1)])  # (node, depth)

    while queue:
        node, depth = queue.popleft()

        # Check if it's a leaf node
        if not node.left and not node.right:
            return depth

        # Add left child to queue if it exists
        if node.left:
            queue.append((node.left, depth + 1))

        # Add right child to queue if it exists
        if node.right:
            queue.append((node.right, depth + 1))

    return 0  # This line is never reached

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(minDepth(root))  # Output: 2
    
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    
    print(minDepth(root))  # Output: 5