# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def check_leaf(root,lis):
            # print(lis)
            if root==None:
                return 
            if root.left==None and root.right==None:
                lis.append(root.val)
                # print(lis)
                return lis
            check_leaf(root.left,lis)
            check_leaf(root.right,lis)
            return lis
        
        lis1=check_leaf(root1,[])
        lis2=check_leaf(root2,[])
        print(lis1)
        print(lis2)
        return lis1==lis2
            
        