class Stack(object):
    def __init__(self):
        self.stack=[]
        
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        self.stack.pop()
        
    def isempty(self):
        return (self.stack==[])
        
    def top(self):
        # if self.isempty():
        #     return False
        return self.stack[-1]
            
        
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic=dict()
        s=Stack()
        
        for items in nums2:
            # print(items)
            # print(s.top)
            while(not s.isempty() and s.top()<items):
                # print("enter")
                dic[s.top()]=items
                s.pop()
            s.push(items)
        
        output=[]
        
        for items in nums1:
            if items not in dic:
                output.append(-1)
            else:
                output.append(dic[items])
                
        return output
        
