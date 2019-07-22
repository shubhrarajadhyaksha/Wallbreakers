# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==0 or k==1:
            return head
        # prev=None
        cur=head
        first=True
        P=head
        total=0 
        c=head
        while(c!=None):
            total+=1
            c=c.next
        if total<k:
            return head
        while(True):
            if cur==None:
                return head
            
            count=0
            prev=None
            start=cur
            if total<k:
                P.next=cur
                return head
            
            while count<k and cur!=None:
                nex=cur.next
                cur.next=prev
                prev=cur
                cur=nex
                count+=1
            # P=prev
            if first:
                head=prev
                first=False
            else:
                P.next=prev
            P=start
            total-=k
                
            
            # prev=start
            
        return head
                
            
                
            
                
                
            
            
        