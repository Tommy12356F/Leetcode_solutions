class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for i in nums:
            if nums.count(i)%k==0:
                c+=i
        return c        