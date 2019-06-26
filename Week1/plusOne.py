class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        l=len(digits)-1
        for i in range(l,-1,-1):
            digits[i]=digits[i]+carry
            carry=digits[i]//10
            digits[i]=digits[i]%10
            
        if carry==1:
            return [1]+digits
        else:
            return digits

#Note: This is like regular addition. So started from last node. 