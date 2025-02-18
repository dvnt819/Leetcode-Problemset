class Solution(object):
    def threeSumClosest(self, nums, target):
        nums=sorted(nums)
        closest_sum=float('inf')
        n=len(nums)

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left=i+1
            right=n-1

            while(left<right):
                current_sum=nums[i]+nums[left]+nums[right]

                if abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum=current_sum

                if(current_sum == target):
                    return current_sum
                elif(current_sum>target):
                    right-=1
                else:
                    left+=1

        return closest_sum

        
