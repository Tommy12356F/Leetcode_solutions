class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        for i in range(0,len(nums),2):
            sum+=nums[i]
            sum-=nums[i-1]
        if len(nums)%2!=0:
            sum+=nums[len(nums)-1]
        return sum