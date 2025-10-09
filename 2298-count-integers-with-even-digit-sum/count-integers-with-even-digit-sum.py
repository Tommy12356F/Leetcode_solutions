class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        def digitsum(x):
            L=[]
            for j in range(len(str(x))):

                    L.append(int(str(x)[j]))
            return sum(L)
        for i in range(1,num+1):
            if digitsum(i)%2==0:
                count+=1
        return count