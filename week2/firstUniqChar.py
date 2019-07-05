import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=collections.Counter(s)
        print(c)
        for index,item in enumerate(s):
    
            if c[item]==1:
                return index
        return -1
        
        # print(c)
        
        
#         dic={}
        
#         for item in s:
#             if item not in dic:
#                 dic[item]=1
#             else:
#                 dic[item]+=1
        
#         for index,item in enumerate(s):
#             if item in dic and dic[item]==1:
#                 return index
#         return -1

            
                
# Note : I first did it without using counters and then I used counters