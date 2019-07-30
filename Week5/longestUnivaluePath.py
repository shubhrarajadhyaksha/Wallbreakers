# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root==None or (root.left==None and root.right==None):
        #     return 0
        self.ans=0
        def path(node):
            x=0
            l,r=False,False
            if node==None:
                return 0
            
            L=path(node.left)
            R=path(node.right)
            
            if L==0 and R==0:
                return 1
            
            if node.left==None or node.left.val==node.val:
                l=True
                
            if node.right==None or node.right.val==node.val:
                r=True
                
            if l==True and r==True :
                self.ans=max(self.ans,1+L+R)
                return 1+max(L,R)
            
            
            elif l is True:
                self.ans=max(self.ans,1+L)
                return 1+L
                
            elif r is True:
                self.ans=max(self.ans,1+R)
                return 1+R
            
            else:
                return 1 
        
        path(root)
        return max(self.ans-1,0)
                    
                
                
            
                
                
        