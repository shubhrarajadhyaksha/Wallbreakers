# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root==None:
            return 0 
        self.ans=1
        
        def find_depth(root):
            if root==None:
                return 0 
            L=find_depth(root.left)
            R=find_depth(root.right)
            
            self.ans=max(self.ans,1+L+R)
            return max(L,R)+1
        
        find_depth(root)
        return self.ans-1
            
       
    
            
            
        