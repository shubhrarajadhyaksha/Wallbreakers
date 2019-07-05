class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy=set()
        for i in candies:
            candy.add(i)
        divide=len(candies)//2
        
        return min(divide,len(candy))

#Note: I was confused earlier about the question. I was creating hashmap. 