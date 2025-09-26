# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=n
        b=False
        high,lower=0,0

        while b==False:
            if guess(a)==-1:
                high = a
            elif guess(a)==1:
                lower = a
            else:
                return a
            a= (high+lower)//2

        