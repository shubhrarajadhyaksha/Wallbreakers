class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # num=128
        # fixed=128
        def isself(number):
            if number==0:
                return False
            fixed=number
            num=number
            while True:
                if num==1 or num==0:
                    return True
                last=num%10
                if last==0:
                    return False
                if fixed%last!=0:
                    return False

                num=(num-last)/10
        # print(isself(128))
        # print(isself(120))
        # print(isself(122))
        # print(isself(2))
        lis=[]
        for item in range(left,right+1):
            if(isself(item)):
                lis.append(item)
        return lis
        
        # Note: This seemed like the only way. Check all the numbers in range left to right and see if they are self dividing. If yes, add them to the list.