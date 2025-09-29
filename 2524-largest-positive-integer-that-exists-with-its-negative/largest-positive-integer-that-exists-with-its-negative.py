class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=-1
        for i in nums:
            if -1*i in nums and i>max:
                max=i
        return max