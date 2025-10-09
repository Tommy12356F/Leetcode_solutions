class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in nums:
            
                for j in range(len(str(i))):

                    L.append(int(str(i)[j]))
        return L
        
