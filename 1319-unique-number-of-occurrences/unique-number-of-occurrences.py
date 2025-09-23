class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        A=[]
        B=[]
        for i in arr:
            if i not in A:
                A.append(i)
                if arr.count(i) not in B:

                    B.append(arr.count(i))
                else:
                    print(A)
                    print(B)
                    return False
        return True


        