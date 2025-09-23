class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxc=0
        for i in range(0,len(nums)-1):
            a=abs(nums[i+1]-nums[i])
            if a>maxc:
                maxc=a
        return max(abs(nums[len(nums)-1]-nums[0]),maxc)