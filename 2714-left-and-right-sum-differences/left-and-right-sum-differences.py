class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftSum=[0]
        rightSum=[0]
        L=[]
        
        for i in range(1,len(nums)):
            
            leftSum.append(sum(nums[0:i]))
        nums.reverse()
        for i in range(1,len(nums)):
            rightSum.append(sum(nums[0:i]))
        rightSum.reverse()

        print(rightSum)
        #return leftSum
        for i in range(len(rightSum)):
            L.append(abs(rightSum[i]-leftSum[i]))
        return L
        
