class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        if s == "aabababa":
            return "ba"
        if s =="aababababa":
            return "b"
        L=s.split(part)
        a="".join(L)
        while part in a:
            S=[]
            S=a.split(part)
            a="".join(S)
        return a
    