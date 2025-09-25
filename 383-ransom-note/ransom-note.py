class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a=list(magazine)
        #a=True
        #return a
        for i in ransomNote:
            if i in a:
                a.remove(i)
            else:
                return False
        return True
        