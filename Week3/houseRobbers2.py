class Solution(object):
    def house_robbers(self,array,start,end):
        prev=0 
        current=0
        for i in range(start,end):
            temp=current
            current=max(prev+array[i],current)
            prev=temp
            
        return current
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0 
        
        if len(nums)==1: 
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        
        else:
            x=self.house_robbers(nums,0,len(nums)-1)
            y=self.house_robbers(nums,1,len(nums))
            return max(x,y)
        
        
        
        
        
        
        