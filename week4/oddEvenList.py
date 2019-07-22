

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or head.next==None or head.next.next==None:
            return head 
        
        cur=head.next.next
        count=0
        prev1=head
        prev2=head.next
        odd=prev2
        
        while(cur!=None):
            temp=cur.next
            if count%2==0:
                prev1.next=cur
                prev1=cur
                prev1.next=None
            else:
                prev2.next=cur
                prev2=cur
                prev2.next=None
                
            cur=temp
            count+=1
        prev2.next=None   
        prev1.next=odd
        
        return head
                
        
       
            
            
            
        