class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        S=[]
        for i in range(0,len(s),k):
            j=""
            j+=s[i]
            for a in range(1,k):

                if i+a<=len(s)-1:
                    j+=s[i+a]
                else:
                    j+=fill
                # if i+2<=len(s)-1:
                #     j+=s[i+2]
                # else:
                #     j+=fill
            S.append(j)
            
        return S
            

            
        