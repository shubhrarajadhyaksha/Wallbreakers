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
        return (self.stack==[])
    
    def top(self):
        return self.stack[-1]
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1=Stack()
        self.st2=Stack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st1.push(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.st1.is_empty():
            return False
        while(not self.st1.is_empty()):
            self.st2.push(self.st1.pop())
        ans=self.st2.pop()
        
        while(not self.st2.is_empty()):
            self.st1.push(self.st2.pop())
        return ans
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.st1.is_empty():
            return False
        while(not self.st1.is_empty()):
            self.st2.push(self.st1.pop())
        ans=self.st2.top()
        
        while(not self.st2.is_empty()):
            self.st1.push(self.st2.pop())
        return ans
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return (self.st1.is_empty())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()