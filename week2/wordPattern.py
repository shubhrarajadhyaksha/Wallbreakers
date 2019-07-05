class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hm={}
        st=set()
        
        sec=str.split()
        if len(sec)!=len(pattern):
            return False
        
        for i in range(len(sec)):
            if pattern[i] not in hm:
                if sec[i] in st:
                    return False
                hm[pattern[i]]=sec[i]
                st.add(sec[i])
                
            else:
                if hm[pattern[i]]!=sec[i]:
                    return False
                
        return True
                    
#This was very similar to previous question I solved. 
#Hashmap and set helps in these 
