import math
class Solution(object):
    def findNumbers(self, nums):
        res=0
        for i in nums:
            length= math.floor(math.log10(i))+1
            if length%2==0:
                res=res+1
        return res
            
        
