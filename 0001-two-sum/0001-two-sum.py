class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        freq={}

        for idx,val in enumerate(nums):
            diff=target-val
            if diff in freq:
                return [freq[diff],idx]

            freq[val]=idx