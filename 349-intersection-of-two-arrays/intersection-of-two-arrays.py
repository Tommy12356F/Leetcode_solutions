class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in nums1:
            if i in nums2 and i not in L:
                L.append(i)
        return L
        