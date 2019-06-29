class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num=x^y
        # print(num)
        count=0
        i=0
        while(i<=31):
            x=(num&(1<<i))>>i
            if x==1:
                count+=1
            i+=1
        return(count)
        
            
            
    '''
    Note:
    #To find the distance between two numbers, we can just exor those, to count the number of 1s in the output was the next challenge
    '''