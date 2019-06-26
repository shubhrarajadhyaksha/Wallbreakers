class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def all_small(word,n):
            # print("Entered all small check")
            for items in word[n:]:
                if ord(items) not in range(97,123):
                    return False
            return True 
        
        def all_capital(word,n):
            # print("Entered all capital check")
            for items in word[n:]:
                if ord(items) not in range(65,91):
                    return False
                # if 65>ord(items)>90:
                    
            return True
        if len(word)<=1:
            return True
        if 97<=ord(word[0])<=122:
            # print("First letter is small")
            return all_small(word,1)
        if 65<=ord(word[0])<=90:
            # print("First letter is capital")
            return all_small(word,1) or all_capital(word,1)
        
#If the first letter is small, all the other letters have to be small
#If the first letter is capital, all the other letters need to be either all small or all capital