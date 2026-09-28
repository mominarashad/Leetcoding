class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len=float("-inf")
        num_set=set(nums) 
        for ch in num_set:

            if ch-1 not in num_set:
                length=0

                while length+ch in num_set:
                    length+=1

                max_len=max(max_len,length)

        return max_len if max_len!=float("-inf") else 0