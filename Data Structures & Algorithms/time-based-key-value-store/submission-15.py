from collections import defaultdict
class TimeMap:
    
    def __init__(self):
        self.timestamps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps: 
            return "" 
        
        candidates = self.timestamps[key]
        l, r = 0, len(candidates) - 1

        res = ""
        while l <= r: 
            m = (l + r) // 2
            if candidates[m][0] > timestamp: 
                r = m - 1
            elif candidates[m][0] < timestamp: 
                res = candidates[m][1]
                l = m + 1
            elif candidates[m][0] == timestamp: 
                return candidates[m][1]
        
        return res