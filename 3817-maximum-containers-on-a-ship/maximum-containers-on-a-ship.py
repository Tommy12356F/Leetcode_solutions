class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        # i=1
        # while i*w<=maxWeight and i<=n**2:
        #     i+=1
        # return i
        maxc=maxWeight//w
        return min(maxc,n**2)
        