class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math

        heap = []

        for point in points: 
            x, y = point[0], point[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (-dist, (point[0], point[1])))
            
            if len(heap) > k: 
                heapq.heappop(heap)
        
        result = []
        while heap: 
            points = heapq.heappop(heap)
            result.append(points[1])
        
        return result
            


        