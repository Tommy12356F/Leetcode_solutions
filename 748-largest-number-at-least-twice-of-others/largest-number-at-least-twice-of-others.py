class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        b=nums.index(a)
        nums.remove(a)
        c=max(nums)
        if a>=2*c:
            return b
        else:
            return -1