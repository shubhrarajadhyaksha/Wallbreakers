class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[None for i in range(len(nums))]
        return_list=[]
        
        def helper(array,subset,index):
            if index==len(nums):
                l=[]
                for items in subset:
                    if items!=None and items not in return_list:
                        l.append(items)
                return_list.append(l)
                
            else:
                subset[index]=None
                helper(array,subset,index+1)
                subset[index]=array[index]
                helper(array,subset,index+1)
                
        helper(nums,subset,0)
        return return_list
                
                        
                
            
        