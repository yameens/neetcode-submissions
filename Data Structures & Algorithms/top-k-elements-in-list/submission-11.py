class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict

        heap = []
        result = []

        frequency = defaultdict(int)
        for num in nums: 
            frequency[num] += 1
        
        for num in frequency.keys(): 
            heapq.heappush(heap, (frequency[num], num))
            if len(heap) > k: 
                heapq.heappop(heap)
        
        while heap: 
            value = heapq.heappop(heap)
            result.append(value[1])
        
        return result

        