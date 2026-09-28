class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        max_sum=float("-inf")
        sum=0
        for i in range(len(nums)):

            sum+=nums[i]

            max_sum=max(max_sum,sum)

            if sum<0:
                sum=0

        return max_sum