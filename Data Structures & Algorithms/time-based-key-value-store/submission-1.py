class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.map.get(key, []) ## initialize just in case
        result = ""

        l, r = 0, len(arr) - 1
        while l <= r: 
            middle = (l + r) // 2
            if arr[middle][1] <= timestamp: 
                result = arr[middle][0]
                l = middle + 1
            else: 
                r = middle - 1
        return result
        
