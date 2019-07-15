class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not s or not g:
            return 0
        child=sorted(g)
        cookies=sorted(s)
        content=0 
        s_cookie=0 
        s_child=0
        
        while(s_child<len(child) and s_cookie<len(cookies)):
            if child[s_child]<=cookies[s_cookie]:
                s_child+=1
                s_cookie+=1
                content+=1
            
            elif child[s_child]>cookies[s_cookie]:
                s_cookie+=1
                
        return content
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if g is None or s is None:
#             return 0 
#         g.sort()
#         s.sort()
#         g_start,g_end=0,len(g)
        
#         for item in s:
#             if g_start<g_end and g[g_start]<=item:
#                 g_start+=1
#         return g_start
#         c=sorted(g)
#         cookies=sorted(s)
        
#         count=0
#         x=len(c)
#         i= 0 
#         while(i<=x): 
#             # print(i)
#             # print(c)
#             # print(cookies)
            
#             if (len(cookies)==0 or i>=len(c)):
#                 # print("Out of range for cookies")
#                 return count
#             else:
#                 # print("c[i]=",c[i])
#                 # print("cookies[i]",cookies[0])
#                 if (c[i]<=cookies[0]):
                    
#                     i=i+1
#                     count=count+1
#                     # c.pop(0)
#                     cookies.pop(0)
                
                 
#                 else:
#                     cookies.pop(0)
#         return count 
                 
                    
                 
                    
        