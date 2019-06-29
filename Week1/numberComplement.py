class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return None
        #length can be 1 or more 
        l=1
        while(l<num):
            l=l<<1|1
        
        return num^l
        
#         idx=-1
#         i=0
#         while(i<32):
#             if (num & 1<<i)>>i==1:
#                 idx+=1
#             i+=1
            
#         val=-1
#         i=0
#         while(i<=32 and val<idx+1):
            
#             num=~(num & 1<<i)>>i
#             i+=1
#             val+=1
#             print(num)
            
#         print(num)
                
#Note:
'''
 New thing I learnt after trying bit shift a lot of times: 
number XOR with 111...... will give complement of the number :

For example : 
000 XOR 111 = 111
111 XOR 111=  000
But in this, we do not know the length of the binary number, ignoring the zeroes in front. I was trying to find the index of the first one.  But then I learnt this method and it made so much sense. 
'''