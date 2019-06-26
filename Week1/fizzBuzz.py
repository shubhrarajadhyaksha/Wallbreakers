class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num=[None for i in range(n)]
        
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                num[i-1]="FizzBuzz"
            elif i%5==0:
                num[i-1]="Buzz"
            elif i%3==0:
                num[i-1]="Fizz"
            else:
                num[i-1]=str(i)
        return num
        
#Note: This was very straightforward. Just did whatever was asked. 