class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A or len(A)==1:
            return A
        i=0
        j=len(A)-1
        
        while(j>i):
            while(A[i]%2==0):
                
                i+=1
                if i>=len(A):
                    return A
            while(A[j]%2!=0):
                
                j-=1
                if j<0:
                    return A
                
            if j>i:
                temp=A[i]
                A[i]=A[j]
                A[j]=temp
                i+=1
                j-=1
        
        return(A)
                
#         i=0
#         j=len(A)-1
        
#         while(j>i):
#             while(A[i]%2==0):
#                 i=i+1


# Note: [When I saw this problem I thought that this can be done in different ways:
#1) Create separate lists for even and odd. Put the answers in a third list and return. But this would take more space. 
#2) To keep two pointers, like pointing to first and second and checking in the go. But this seemed little complicated for me compared to the method I did. 
#3) Start two pointers from two ends as this will be the simplest thing to do. 
            
            
        