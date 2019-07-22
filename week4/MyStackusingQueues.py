class Node(object):
    def __init__(self,val=None):
        self.val=val
        self.next=None
        self.top=None
        
class Queue(object):
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def enq(self,val):
        n=Node(val)
        self.top=val
        if self.length==0:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
            
        self.length+=1
        
    def dq(self):
        val=self.head.val
        self.head=self.head.next
        self.length-=1
        if self.length==0:
            self.tail=None
        return val
    
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1=Queue()
        self.q2=Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.enq(x)
        # q1.top=x
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while(self.q1.length>1):
            self.q2.enq(self.q1.dq())
        val=self.q1.dq()
        
        while(self.q2.length!=0):
            self.q1.enq(self.q2.dq())
        return val
        
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1.top
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.length==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()