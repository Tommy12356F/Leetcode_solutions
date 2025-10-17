class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        balance=0

        for i in range(len(s)):
            if s[i]=="L":
                balance+=1
            else:
                balance-=1
            if balance==0:
                count+=1
        return count
            
        