class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if not nums:
        #     return -1
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        
        
        dic={}
        
        for i in range(0,len(nums)):
            
            if target-nums[i] in dic:
                return[dic[target-nums[i]],i]
            if nums[i] not in dic:
                dic[nums[i]]=i
                
    
                
                
                 
                
            
#Note: If one number is given and we have to find if this number and some other number is equal to a particular sum, 
#we can create a dictionary or a set and see if the other number exists in the set or dictionary. 
#Dictionary is better as we can store the index along with the number. 