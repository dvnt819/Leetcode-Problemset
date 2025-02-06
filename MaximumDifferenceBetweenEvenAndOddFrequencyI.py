from collections import Counter
class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        f=Counter(s)
        even=[]
        odd=[]
        for count in f.values():
            if count % 2 == 0:
                even.append(count)
            else:
                odd.append(count)

        if not even or not odd:
            return -1
        return max(odd)-min(even)
