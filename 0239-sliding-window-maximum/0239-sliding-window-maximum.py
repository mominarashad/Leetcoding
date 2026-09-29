class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        n=len(nums)

        res=[0]*(n-k+1)

        dq=deque()

        for i in range(k):

            while dq and nums[i]>=nums[dq[-1]]:
                dq.pop()

            dq.append(i)

        res[0]=nums[dq[0]]

        for i in range(k,n):

            if dq[0]<i-k+1:
                dq.popleft()

            while dq and nums[i]>=nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            res[i-k+1]=nums[dq[0]]

        return res


        

