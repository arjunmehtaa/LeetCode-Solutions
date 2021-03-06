# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity   : O(N)
# Space Complexity  : O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return traverseTree(root, -inf, inf)

def traverseTree(node, min, max):
    if node.val <= min or node.val >= max:
        return False
    if node.left:
        if not traverseTree(node.left, min, node.val):
            return False
    if node.right:
        if not traverseTree(node.right, node.val, max):
            return False
    return True
        
        