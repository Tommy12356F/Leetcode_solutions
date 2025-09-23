class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        A=[]
        B=[]
        S=[]
        for i in nums1:
            if i not in nums2 and i not in A:
                A.append(i)
        for i in nums2:
            if i not in nums1 and i not in B:
                B.append(i)
        S.append(A)
        S.append(B)
        return S