class stack(object):
    def __init__(self):
        self.l=[]
        
    def push(self,val):
        self.l.append(val)
        
    def pop(self):
        self.l.pop()
        
    def top2sum(self):
        return self.l[-1]+self.l[-2]
        
    
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        S=stack()
        total=0
        for item in ops:
            if item[0]=="-":
                op=-int(item[1:])
                S.push(op)
                
            elif item.isdigit():
                op=int(item)
                S.push(op)
                
            elif item=="D":
                op=2*S.l[-1]
                S.push(op)
                
            elif item=="+":
                op=S.top2sum()
                S.push(op)
                
            elif item=="C":
                op=-S.l[-1]
                S.pop()
                
            total+=op
            # print(total)
            
        return total
                
                
                
                
        
        
        
        
        
        
        
        
        