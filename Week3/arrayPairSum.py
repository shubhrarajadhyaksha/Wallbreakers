class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        
        index,count=0,0
        
        while(index<len(nums)-1):
            count+=min(nums[index],nums[index+1])
            index+=2
            
        return count
        
        