"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: 
            return True

        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end

        for i, interval in enumerate(intervals): 
            if i > 0: 
                newStart = interval.start
                if end > newStart: 
                    return False
                else: 
                    end = interval.end
        
        return True
            
