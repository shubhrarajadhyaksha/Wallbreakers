class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        XOR=0
        for item in nums:
            XOR=XOR^item
        # print(XOR)
        return XOR
#         nums.sort()
#         #print len(nums)
#         if len(nums)==1:
#             # print(nums[0])
#             return nums[0]
        
#         for item in range(1,len(nums)-1):
#             # print ("item",item)
#             # print ("nums[item-1]",nums[item-1])
#             # print ("nums[item]",nums[item])
#             # print ("nums[item+1]",nums[item+1])
            
            
#             if item==1 and nums[item]!=nums[item-1]:
#                 # print("here")
#                 return nums[0]
#             elif nums[item]!=nums[item-1] and nums[item]!=nums[item+1]:
#                 # print("true",nums[item]," ",nums[item-1]," ",nums[item+1])
#                 return nums[item]
#         print("Final")    
#         return nums[-1]
        

# Note: My first thought was to use a hash table. But then it would have been  o(n) time and 0(n) space. Second I thought about sorting , but still I would not help. So I read about the bit manipulations and this stuck me. 
#We can XOR 2 same elements to get 0 and 0 XORd with any element given the number itself. So the extra number will be returned using this. 