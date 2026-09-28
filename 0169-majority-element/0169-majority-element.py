class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        freq={}

        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        for val,fre in freq.items():
            if fre>(n/2):
                return val