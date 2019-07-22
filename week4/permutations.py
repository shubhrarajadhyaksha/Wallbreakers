class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            yield []
        if len(nums)==1:
            yield nums
        
        else:
            # l=[]
            for i in range(len(nums)):
                x=nums[i]
                xs=nums[:i]+nums[i+1:]
                for p in self.permute(xs):
                    # print(p)
                    yield([x]+p)
                    
            # return l 
            
        