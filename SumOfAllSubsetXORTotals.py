class Solution(object):
    def subsetXORSum(self, nums):
        return reduce(or_, nums)<<(len(nums)-1)
        
