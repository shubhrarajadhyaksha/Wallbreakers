# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or head.next==None:
            return head
       
        prev=None
        cur=head
        while(cur!=None):
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        head=prev
        
        return head
        
            
        