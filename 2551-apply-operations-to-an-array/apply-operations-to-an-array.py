class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for i in nums:
            if i!=0:
                L.append(i)

        for i in range(len(nums)-len(L)):
            L.append(0)
        return L
