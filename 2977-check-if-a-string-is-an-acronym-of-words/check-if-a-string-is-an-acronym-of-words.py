class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        b=""
        for i in words:
            b+=i[0]
        return b==s