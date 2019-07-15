class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
                return 0 
            
        if len(nums)==1:
                return nums[0]
            
        if len(nums)==2:
                # prev=array[1]
                return max(nums[0],nums[1])
        def check_max(array):
            
            
            this=array[0]
            if len(array)==1:
                prev=0
                current=array[0]
                return prev,current
            # if len(array)==2:
            #     prev=array[1]
            #     cur=array[0]
            #     return prev,cur,max(array[0],array[1])
            
            prev,cur=check_max(array[1:])
            temp=cur
            cur=max(cur,prev+this)
            prev=temp
            return prev,cur
            # maxm=max(maxm,prev+current)
            # prev=cur
            # cur=current
            # # print(prev,maxm)
            # print(prev,cur,maxm)
            # return prev,cur,maxm
        
        p,cur=check_max(nums[:len(nums)-1])
        p1,cur1=check_max(nums[1:])
        # print(m1)
        # print(m2)
        return(max(cur,cur1))
            
            
            
            
                
        