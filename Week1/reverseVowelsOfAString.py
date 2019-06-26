class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        start=0
        end=len(s)-1
        st=[i for i in s]
        while(end>start):
            if st[start] in vowels and st[end] in vowels:
                temp=st[start]
                st[start]=st[end]
                st[end]=temp
                start+=1
                end-=1
            elif st[start] in vowels and st[end] not in vowels:
                end-=1
            elif st[start] not in vowels and st[end] in vowels:
                start+=1
            
            else:
                start+=1
                end-=1
        return "".join(st)
                
        
            
            
        
#Note:The approach I used was very simple two pointer approach. One pointer starting from front and second from the end. 