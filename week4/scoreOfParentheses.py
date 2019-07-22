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
    
    def top(self):
        return self.stack[-1]
    
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        st=Stack()
        
        for item in S:
            if item=="(":
                st.push(item)
                
            elif item==")":
                sm=0
                if st.top()=="(":
                    st.pop()
                    st.push(1)
                
                else:
                    while(st.top()!="("):
                        sm=sm+st.pop()
                    st.pop()
                    st.push(sm*2)
        ans=0
        while(not st.is_empty()):
            ans+=st.pop()
            
        return ans
                    
                
            
                
            