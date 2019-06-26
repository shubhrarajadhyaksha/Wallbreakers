class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s)==1:
            return s
        def reverse(string,start,end):
            while(start<end):
                temp=string[start]
                string[start]=string[end]
                string[end]=temp
                start+=1
                end-=1
                
        # xyz=["P","A","M","I"]
        # reverse(xyz,0,2)
        # reverse(xyz,0,1)
        # print(xyz)
        rev=[item for item in s]
        # print(rev)
        
        start=0
        # end=0
        for i in range(len(rev)):
            if i==len(rev)-1:
                reverse(rev,start,i)
                return "".join(rev)
            
            elif rev[i]!=' ':
                end=i
                
            else:
                reverse(rev,start,end)
                start=end+2
                
            
            
            
        
        #Note:I did the same code in 2 ways. One using the inbuilt split function and reverse and once from scratch. 
        '''
        class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        list_of_words=s.split(' ')
        print(list_of_words)
        
        rev=[]
        for word in list_of_words:
            rev.append(word[::-1])
            
        # for ind,word in enumerate(list_of_words):
        #     # rev.append(word[::-1])
        #     list_of_words[ind]=word[ : :-1]
        
        # return " ".join(list_of_words)
        return " ".join(rev)
        '''