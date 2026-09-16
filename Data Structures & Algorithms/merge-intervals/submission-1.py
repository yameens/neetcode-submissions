class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## queue is not the method, we can adjust it by simply looking at the most recent interval 
        if not intervals: 
            return []

        intervals.sort()
        merged = []
        start, end = intervals[0][0], intervals[0][1]

        for i, interval in enumerate(intervals): 
            if i > 0: 
                newStart, newEnd = interval[0], interval[1]
                if end >= newStart: 
                    end = max(end, newEnd)
                else: 
                    merged.append([start, end])
                    start = newStart
                    end = newEnd
        
        merged.append([start, end])
        
        return merged
            


        