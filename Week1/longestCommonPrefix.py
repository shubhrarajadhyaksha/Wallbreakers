class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        
        first=strs[0]
        mx_len=len(strs[0])
        for items in range(1,len(strs)):
            mx_len=min(mx_len,len(strs[items]))
        if mx_len==0:
            return ""
        max_len=None
        for i in range(1,len(strs)):
            if max_len==0:
                return ""
            second=strs[i]
            count=0
            for j in range(0,mx_len):
                if first[j]==second[j]:
                    count+=1
                else:
                    break
            if max_len==None:
                max_len=count
            
            else:
                max_len=min(count,max_len)
        
        return strs[0][:max_len]
                
                    
                
        
#Note: The longest common prefix cannot be longer than the shortest string.  I used this to check each item in the list and compare it with the previous one. 