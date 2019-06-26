def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(A), len(A[0])
        # if rows==cols:
        #     matrix()
        B = [[0 for x in range(rows)] for y in range(cols)]
        # print(B)
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                # print('i=%d, j=%d' % (i, j))
                # print("A[i][j]", A[i][j])
                B[j][i] = A[i][j]
            #     print(B[j][i])
            #     print(B)
            # print(B)
        return B

#I was first trying to do it in place. Then I remembered that the dimensions of array might change as it is not N*N matrix. 
#So I created a new 2D matrix with opposite dimensions. 
#One more problem I faced when creating 2D array. 
#B = [[0 for x in range(rows)] for y in range(cols)] 
#Instead of using above method, I was using B = [[None]*len(A)]*len(A[0])
#Then I learnt the concept of shallow pointer in python