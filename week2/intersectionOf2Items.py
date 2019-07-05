class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # nums1=list(set(nums1))
        # l=[]
        # for item in list(set(nums2)):
        #     if item in nums1:
        #         l.append(item)
        # return l 
        hash_f={}
        
        for item in nums1:
            if item not in hash_f:
                hash_f[item]=True
        
        i=[]
        
        for item in nums2:
            if item in hash_f and item not in i:
                i.append(item)
        return i
                
#All items in 1st array which are also in the second array. 
