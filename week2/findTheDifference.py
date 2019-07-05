import collections
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_count=collections.Counter(s)
        t_count=collections.Counter(t)
        x=t_count-s_count
        for item in x:
            return item
        
        
        