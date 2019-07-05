from collections import defaultdict

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        first,second=None,None
        n=len(nums)
        lis=[i for i in range(1,n+1)]
        ans = defaultdict(int)
        
        for i in nums:
            ans[i]+=1
            
            if ans[i]==2:
                first=i
        for i in range(1,n+1):
            if i not in ans:
                second=i
                break
        
        return([first,second])
                
            
        

        
        
        
        
     
            
        
#         if not nums:
#             return []
#         n=len(nums)
#         expected_sum=n*(n+1)/2
        
#         nums=sorted(nums)
#         prev=nums[0]
#         extra=0
#         total=sum(nums)
#         for j in range(1,n):
            
#             if prev==nums[j]:
#                 extra=prev
#                 break
#             prev=nums[j]
#         missed=expected_sum-(total-extra)
#         return [extra,missed]


        
        
                
        
        