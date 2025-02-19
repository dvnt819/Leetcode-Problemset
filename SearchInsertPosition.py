class Solution(object):
    def searchInsert(self, nums, target):
        nums.append(target)
        nums=sorted(nums)
        return nums.index(target)
                
        
