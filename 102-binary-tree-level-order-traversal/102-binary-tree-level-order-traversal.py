# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right   

# Time Complexity   : O(N)
# Space Complexity  : O(N)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while len(queue):
            size = len(queue)
            count = 0
            sub = []
            while count < size:
                node = queue.pop(0)
                sub.append(node.val)
                count += 1
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sub)
        return res