class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        x=set()
        for item in J:
            x.add(item)
            
        count=0
        for item in S:
            if item in x:
                count+=1
        
        return count
        
        
#Note: Just used a set so that can search for jewel in O(1) time