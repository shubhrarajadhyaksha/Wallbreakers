class Node(object):
    def __init__(self):
        self.children={}
        self.end=False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()
        
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur=self.root
        
        for letter in word:
            if letter not in cur.children:
                cur.children[letter]=Node()
            cur=cur.children[letter]
        cur.end=True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur=self.root
        for letter in word:
            # print(letter)
            if letter not in cur.children:
                return False
            cur=cur.children[letter]
        return cur.end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur=self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur=cur.children[letter]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)