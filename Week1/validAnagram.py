class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s=sorted(s)
        # t=sorted(t)
        # if s==t:
        #     return True
        # return False
        
        hm={}
        for i in s:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
                
        for i in t:
            if i not in hm:
                return False
            hm[i]-=1
            if hm[i]==-1:
                return False
            
        for items in s:
            if hm[items]!=0:
                return False
        return True
            
            
        
            
#Note : First thought: To check if anagrams, we can sort both the strings and see if they are same.
# Other option is to use hashmap. 