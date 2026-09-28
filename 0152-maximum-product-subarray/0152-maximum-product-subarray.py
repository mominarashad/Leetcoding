class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        curr_max=curr_min=best=nums[0]

        for ch in nums[1:]:
            candidates=[ch,ch*curr_max,ch*curr_min]

            curr_max=max(candidates)
            curr_min=min(candidates)

            best=max(curr_max,best)

        return best