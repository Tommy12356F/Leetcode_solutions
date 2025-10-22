class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a=""
        c=1
        while a=="":
            if c*k not in nums:
                a="b"
            else:
                c+=1
        return c*k
