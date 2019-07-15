class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        is_matching= bool(s) and p[0] in (s[0],".")
        
        if len(p)>=2 and p[1]=="*":
            return  (is_matching and self.isMatch(s[1:],p) or (self.isMatch(s,p[2:])))
                    
        else:
                                    return is_matching and self.isMatch(s[1:],p[1:])
            
        