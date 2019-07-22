class Node(object):
    def __init__(self,val=None):
        self.val=val
        self.next=None
        
class Queue(object):
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def enq(self,val):
        n=Node(val)
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
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0 or len(nums)<2 or len(nums)==k:
            return
        while(k>len(nums)):
            k=k-len(nums)
        
        Q=Queue()
        
        for items in nums:
            Q.enq(items)
            
        for i in range(k,len(nums)):
            nums[i]=Q.dq()
        
        for i in range(k):
            nums[i]=Q.dq()
            
            
        
            
        
        
            
            