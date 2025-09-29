class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = [x for x in nums]
        count=0
        for i in range(0, len(nums)):
            if nums.count(nums[i-count])>1:
                nums.remove(nums[i-count])
                count+=1
        return len(nums)