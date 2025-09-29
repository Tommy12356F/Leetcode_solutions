class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        L=[0,32]
        for i in range(len(s)-1):
            if abs(ord(s[i])-ord(s[i+1])) not in L:
                count+=1
        return count