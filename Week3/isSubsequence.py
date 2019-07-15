class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: 
            return True 
        if len(s)>len(t):
            return False
        
        s_start=0
        t_start=0 
        
        while(s_start<len(s) and t_start<len(t)):
            if s[s_start]==t[t_start]:
                s_start+=1
                t_start+=1
            
            else: 
                t_start+=1
                
        if s_start==len(s):
            return True 
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not s:
#             return True
#         if len(s)>len(t):
#             return False
#         j=0
#         for i in range(len(t)):
#             if j>len(s)-1:
#                 break
            
#             if t[i]==s[j]:
#                 j+=1
                
#         if j>len(s)-1:
#             return True
#         return False
            
            
        
        