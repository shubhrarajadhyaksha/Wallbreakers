class Stack(object):
    def __init__(self):
        self.stack=[]
        
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        val=self.stack[-1]
        self.stack.pop()
        return val
    
    def is_empty(self):
        return self.stack==[]
        
    
class Solution:
    def isValid(self, s: str) -> bool:
        d=dict()
        d[')']='('
        d['}']='{'
        d[']']='['
        st=Stack()
        
        for bracket in s:
            if bracket in d:
                if st.is_empty():
                    return False
                b=st.pop()
                if d[bracket]!=b:
                    return False
            
            # if bracket in ["(","{","["]:
            else:
                st.push(bracket)
        
        if not st.is_empty():
            return False
        return True
                
            
                
                
            
        
        
            
        
        