class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # def flip(num):
        #     return 1-num
        for index,arr in enumerate(A):
            i=0
            j=len(A[index])-1
            while(i<=j):
                temp=1-A[index][i]
                A[index][i]=1-A[index][j]
                A[index][j]=temp
                i+=1
                j-=1
        return A

#Note: I was actually thinking of doing everything together. Hence I wrote the flip function. 
#But then I just followed the steps in the explaination. Reverse using A[index][::-1] and then using flip function to flip the numbers. 
#Then I tried 2 pointer method and also flipped while doing the same.