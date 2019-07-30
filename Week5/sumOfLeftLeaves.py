# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root==None or (root.left==None and root.right==None):
            return 0
        
        def add(node,side):
            if node==None:
                return s
            if side=="left" and node.left==None and node.right==None:
                s=node.val
                
                return s
            left=0
            right=0
            if node.left!=None:
                left=add(node.left,"left")
            if node.right!=None:
                right=add(node.right,"right")
            return left+right
               
        s=add(root,"left")
        return s
                
        