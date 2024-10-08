"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = defaultdict(list)
        
        def traverse(node):
            if node.val in nodeMap:
                return nodeMap[node.val]
            newNode = Node(node.val)
            nodeMap[node.val] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(traverse(neighbor))
            return newNode
        
        return traverse(node) if node else None
            
        
        