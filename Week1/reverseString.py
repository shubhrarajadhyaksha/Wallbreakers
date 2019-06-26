class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start=0
        end=len(s)-1
        
        while(start<=end):
            temp=s[start]
            s[start]=s[end]
            s[end]=temp
            start+=1
            end-=1
            
        
#There are python inbuilt methods to do this but I thought that this can be done by using two pointers. 
#One pointing to the start and one at the end and exchanging the letters between the two pointers. 