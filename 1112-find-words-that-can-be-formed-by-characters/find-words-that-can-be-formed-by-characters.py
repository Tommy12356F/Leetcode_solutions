class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        def check(ransomNote):
            a=[]
            a=list(chars)
            #a=True
            #return a
            for i in ransomNote:
                if i in a:
                    a.remove(i)
                else:
                    return False
            return True
        L=[]
        for z in words:
            if check(z)==True:
                L.append(z)
        s=0
        for j in L:
            s+=len(j)
        return s


        
        