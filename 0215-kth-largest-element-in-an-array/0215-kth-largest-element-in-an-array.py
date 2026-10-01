class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        min_heap=[]

        for ch in nums:
            heapq.heappush(min_heap,ch)

            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return min_heap[0]