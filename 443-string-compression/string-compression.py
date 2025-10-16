class Solution(object):
    def compress(self, x):
        """
        :type chars: List[str]
        :rtype: int
        """
        A=[]
        B=[]
        # L=list(chars)
        s=x[0]
        count=1
        # a=L[0]
        # if L[0]==L[-1]:
        #     return L[0]+str(len(L))
        for i in range(1,len(x)):
            if x[i]==s:
                count+=1
            else:
                A.append(s)
                B.append(count)
                count=1
                s=x[i]
        A.append(s)
        B.append(count)
        print(A)
        print(B)
        t=""
        for i in range(len(A)):
            t+=A[i]
            if B[i]>1:
                t+=str(B[i])
        for i in range(len(t)):
            x[i]=t[i]
        
        return len(t)
        

            