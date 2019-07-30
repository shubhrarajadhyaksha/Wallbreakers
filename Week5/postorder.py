"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        val=self.stack[-1]
        self.stack.pop()
        return val
    def isempty(self):
        return self.stack==[]
    
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root==None:
            return []
        lis=[root]
        stack=Stack()
        # stack.push(cur.val)
        while(lis):
            value=lis.pop()
            stack.push(value.val)
            for items in value.children:
                lis.append(items)
        lis=[]        
        while(not stack.isempty()):
            lis.append(stack.pop())
            
        return lis
            
            
            
        
            
        