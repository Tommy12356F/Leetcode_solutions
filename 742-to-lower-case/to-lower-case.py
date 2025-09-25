class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        for i in s:
            a+=i.lower()
        return a

        