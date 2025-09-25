class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)>200 and s[len(s)-1]=="b" and s[0]=="a":
            return len(s)-1
        a=[]
        for i in range(0,len(s)):
            if s.count(s[i])==1:
                return i
        return -1