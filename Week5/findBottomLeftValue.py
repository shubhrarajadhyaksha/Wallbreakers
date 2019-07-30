# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root==None:
            return None
        self.max_level=-1
        self.max_left=None
        def max_left(node,level):
            if node.left==None:
                # if side=="left":
                if level>self.max_level:
                    self.max_level=level
                    self.max_left=node.val
                    
            
            if node.left==None and node.right==None:
                
                if level>self.max_level:
                    self.max_level=level
                    self.max_left=node.val
                return 
            
            if node.left!=None:
                max_left(node.left,level+1)
            if node.right!=None:
                max_left(node.right,level+1)
            
            return 
        
        max_left(root,0)
        
        return self.max_left
        
        
            
        
            
                
        
        
        