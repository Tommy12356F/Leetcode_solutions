class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[]
        for i in range(len(str(n))):
            nums.append(int(str(n)[i]))
        sum=0
        for i in range(0,len(nums),2):
            sum+=nums[i]
            sum-=nums[i-1]
        if len(nums)%2!=0:
            sum+=nums[len(nums)-1]
        return sum