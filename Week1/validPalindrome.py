class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s=s.replace(" ","")
        # s=s.replace(".","")
        # s=s.replace("@","")
        # s=s.replace("#","")
        # s=s.replace(",","")
        # s=s.replace(":","")
        # s=s.replace("?","").lower()
        s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
        # print(s)
        if s==s[::-1]:
            return True
        return False


#I know that to detect palindrome we can see if the word is same as reverse of the word.
# I did not know how to keep just tha alphanumeric characters, so i tried replace method, but then I checked online and used the one word representation. 