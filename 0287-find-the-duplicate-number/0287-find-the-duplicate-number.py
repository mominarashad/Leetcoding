class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        freq={}

        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1


        for ch,fre in freq.items():
            if fre>1:
                return ch