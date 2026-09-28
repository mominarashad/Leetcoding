class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res=set()

        n=len(nums)

        if n<3:
            return []

        for i in range(n-2):

            low=i+1
            high=n-1

            while low<high:

                sum=nums[low]+nums[high]+nums[i]

                if sum==0:
                    res.add((nums[low],nums[high],nums[i]))
                    low+=1
                    high-=1
                elif sum<0:
                    low+=1
                else:
                    high-=1

        return [list(triple) for triple in res]
