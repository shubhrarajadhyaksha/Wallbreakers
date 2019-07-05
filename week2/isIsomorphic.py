class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        hm={}
        st=set()
        
        for i in range(len(s)):
          
            char=s[i]
            replace=t[i]
            if char in hm:
                if hm[char]!=replace:
                    return False
            else:
                if replace in st:
                    return False
                hm[char]=replace
            st.add(replace)
        
        # print(hm)
        return True
                        
        