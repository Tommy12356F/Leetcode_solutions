class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S=list(s)
        T=list(t)
        A=[x for x in S]
        L=[]
        count=0
        for i in range(len(T)):
            if T[i-count] not in S:
                T.remove(T[i-count])
                
                count+=1
            else:
                S.remove(T[i-count])
        print(T)
        print(S)
        return T==A