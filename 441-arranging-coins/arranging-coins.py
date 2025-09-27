class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        level=0
        # if n==1:
        #     return 1
        # if n==3:
        #     return 2
        while n-level>=0:
            n-=level
            level+=1
        return level-1
