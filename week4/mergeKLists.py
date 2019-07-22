# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        l=[]
        
        for lis in lists:
            while lis!=None:
                # print(lis.val)
                l.append(lis.val)
                lis=lis.next
                
        heapq.heapify(l)
        print(l)
        head=None
        
        while len(l)>0:
            val=heapq.heappop(l)
            n=ListNode(val)
            if head is None:
                head=n
                cur=head
            else:
                cur.next=n
                cur=cur.next
                
        return head
        
        
        