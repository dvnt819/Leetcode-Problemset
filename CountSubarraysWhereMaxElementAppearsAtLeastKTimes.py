class Solution(object):
    def countSubarrays(self, nums, k):
        target = max(nums)
        count = 0
        left = 0
        n = len(nums)
        ans = 0
        
        for i in range(n):
            if nums[i] == target:
                count += 1
            while count == k:
                ans += n - i
                if nums[left] == target:
                    count -= 1
                left += 1
        
        return ans
        
