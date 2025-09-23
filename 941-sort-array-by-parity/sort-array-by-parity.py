class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in nums:
            if i%2==0:
                L.append(i)
        for i in nums:
            if i%2!=0:
                L.append(i)
        return L
        