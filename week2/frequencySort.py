import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_count=collections.Counter(s)
        ans=[]
        #print(sorted(key_value.items(), key = 
             #lambda kv:(kv[1], kv[0])))
        for key,val in sorted(s_count.items(),key=lambda i:-i[1]):
            j=0
            while(j<val):
                ans.append(key)
                j+=1
        return "".join(ans)
    
        