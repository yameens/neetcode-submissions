class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq
        heap = [-num for num in nums]
        heapq.heapify(heap)

        while k > 0: 
            res = heapq.heappop(heap)
            k -= 1
            if k == 0: 
                return -res
        
        return 0
        