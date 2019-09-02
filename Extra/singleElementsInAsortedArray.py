class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums)==1:
            return nums[0]
        
        start=0 
        end=len(nums)-1
        while(start<end):
            mid=(end-start)//2+start
            # if start==mid:
            #     return nums[start]
            print("start=",start,"mid=",mid,"end=",end)
            # List is always odd length 
            if mid%2==0:
                if nums[mid-1]==nums[mid]:
                    end=mid-1
                elif nums[mid+1]==nums[mid] :
                    start=mid+1
                else:
                    return nums[mid]
                    
            elif mid%2!=0:
                if nums[mid-1]==nums[mid]:
                    start=mid+1
                else:
                    end=mid-1
            
                    
        return nums[start]