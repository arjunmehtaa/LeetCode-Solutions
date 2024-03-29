# Time Complexity   : O(N)
# Space Complexity  : O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return traverse(p, q)
        
def traverse(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    if p.val != q.val:
        return False
    if not traverse(p.left, q.left) or not traverse(p.right, q.right):
        return False
    return True