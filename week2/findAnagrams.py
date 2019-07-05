import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
            return []
        if s=="" or not s:
            return []
        
        ans=[0 for i in range(26)]
        for letter in p:
            ans[ord(letter)-ord('a')]+=1
            # print(ans)
        # print(ans)
        n=len(p)
        return_list=[]
        ans2=[0 for i in range(26)]
        for i in range(0,len(s)-n+1):
            # print(s[i:i+n])
            if i==0:
                for item in s[0:n]:
                    ans2[ord(item)-ord('a')]+=1
            else:
                ans2[ord(s[i-1])-ord('a')]-=1
                if i+n<(len(s)+1):
                    # print("yes")
                    # print(s[i+n])
                    ans2[ord(s[i+n-1])-ord('a')]+=1
            # print(ans2)
            if ans2==ans:
                # print("yes")
                return_list.append(i)
            
                
                
            
            # ans2=ans
            # for items in s[i:i+n]:
                
            # ans2=[0 for i in range(26)]
            # for letter in s[i:i+n]:
            #     ans2[ord(letter)-ord('a')]+=1
            # # ans2=collections.Counter(s[i:i+n])
            # if ans==ans2:
            #     return_list.append(i)
                
        return return_list
            
        
        
        
        
        
        
        
        