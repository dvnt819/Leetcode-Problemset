class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        y=x
        x=abs(x)
        while x>0:
            s=s*10 + x%10
            x=x//10

        if ((s > (2**31 - 1)) or (s < -2**31)):
            return 0
        if y>=0:
            return s
        else:
            return -1*s
