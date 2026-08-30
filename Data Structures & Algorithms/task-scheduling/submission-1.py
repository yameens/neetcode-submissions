class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import deque, defaultdict

        frequency = defaultdict(int)
        for task in tasks: 
            frequency[task] += 1
        
        heap = []
        for task in frequency.keys(): 
            heapq.heappush(heap, (-frequency[task], task))
        
        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap: 
                freq, task = heapq.heappop(heap)
                freq += 1
                if freq != 0: 
                    queue.append((freq, task, time + n))
            
            if queue and queue[0][2] == time: 
                freq, task, time = queue.popleft()
                heapq.heappush(heap, (freq, task))
        
        return time


             






        


        
        