class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        i=0
        if len(nums)>1:
            while len(a)!=1:
                a=[]
                for i in range(len(nums)-1):
                    a.append((nums[i]+nums[i+1])%10)
                nums=a
                #print(a)
        
        return nums[0]

        