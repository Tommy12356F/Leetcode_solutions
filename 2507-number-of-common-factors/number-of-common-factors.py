class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        A=[]
        B=[]
        for i in range(1,int(a**0.5) +1):
            if a%i==0:  
                A.append(i)
                if a/i not in A:

                    A.append(a/i)
        for i in A:
            if b%i==0:

                B.append(i)
                
        print(A)
        print(B)
        return len(B)
        # count=1
        # for i in range(2,min(a,b)+1):
        #     if a%i==0 and b%i==0:
        #         count+=1
        # return count
