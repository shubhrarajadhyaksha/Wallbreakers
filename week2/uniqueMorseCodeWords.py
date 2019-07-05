class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alpha_list=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        s=set()
        
        for item in words:
            st=[]
            for i in item:
                x=ord(i)-ord('a')
                st.append(alpha_list[x])
            s.add("".join(st))
            
        return len(s)
                
        
#Note: This was very easy 