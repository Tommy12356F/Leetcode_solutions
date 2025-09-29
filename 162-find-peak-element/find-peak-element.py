class Solution(object):
    def findPeakElement(self, mountain):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(mountain)==2:
            return mountain.index(max(mountain))
        L=[]
        for i in range(1,len(mountain)-1):
            if mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]:
                L.append(i)
        if mountain[len(mountain)-1]>mountain[len(mountain)-2]:
            L.append(len(mountain)-1)
        if len(L)==0:
            return 0

        else:
            return L[0]