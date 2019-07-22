import heapq
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k>len(nums):
            return 
        x=collections.Counter(nums)
        l=[]
        for keys,values in x.items():
            l.append([values,keys])
            
        heapq.heapify(l)
        l=heapq.nlargest(k,l)
        
        output=[]
        for item in l:
            output.append(item[1])
        return output
            
        
        
        
        