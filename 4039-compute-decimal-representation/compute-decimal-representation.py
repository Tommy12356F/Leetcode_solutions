class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        L=[]
        l=len(str(n))
        for i in range(l):
            a=0
            a=int(str(n)[i])*10**(l-1-i)
            if a!=0:
                L.append(a)
        return L
