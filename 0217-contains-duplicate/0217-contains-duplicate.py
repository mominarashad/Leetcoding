class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        num_set=set()

        for ch in nums:
            if ch in num_set:
                return True
            num_set.add(ch)
        return False