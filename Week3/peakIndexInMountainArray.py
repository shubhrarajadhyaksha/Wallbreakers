class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start=0 
        end=len(A)-1
        
        while(start<end):
            mid=(start+end)//2
            
            if A[mid]<=A[mid+1]:
                start=mid+1
            else:    
                end=mid
        
        # print(start,end)
        return start
            
        