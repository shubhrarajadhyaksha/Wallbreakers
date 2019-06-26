class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
       
        sm=0  #total sum
        r=0   #raise to
        #BA:26*2+1
        # ABA= 1*26^0+2*26^1+1*26^2
        for item in s[::-1]:
            # print(item)
            val=ord(item)-64
            ans=val*(26**r)
            # print(ans)
            sm=sm+ans
            r=r+1
            
        return(sm)
            
            
        
#Note:I had to understand the conversion first, see what mathematics is applied here. 
#After figuring that out, it was easy. I had to search for ord function, to convert alphabet to ascii value