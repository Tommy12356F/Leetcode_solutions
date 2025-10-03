class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        L=list(word)
        if L[0].isupper()==True:
            if L[-1].isupper()==True:
                for i in L:
                    if i.isupper()==False:
                        return False
            else:
                for i in L[1::]:
                    if i.isupper()==True:
                        return False

        else:
            for i in L:
                if i.isupper()==True:
                    return False
        return True
        