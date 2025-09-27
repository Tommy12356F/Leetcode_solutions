class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S=list(s)
        T=list(t)
        if len(S)!=len(T):
            return False
        for i in S:
            if i in T:
                T.remove(i)
            else:
                return False
        return True
        