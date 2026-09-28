class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()

        res=set()

        n=len(nums)

        if n<4:
            return []

        for i in range(n-3):
            for j in range(i+1,n-2):
                    low=j+1
                    high=n-1

                    while low<high:

                        sum=nums[low]+nums[high]+nums[i]+nums[j]

                        if sum==target:
                            res.add((nums[low],nums[high],nums[i],nums[j]))
                            low+=1
                            high-=1
                        elif sum<target:
                            low+=1
                        else:
                            high-=1

        return [list(triple) for triple in res]
