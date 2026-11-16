class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.store[key]:
            return ""
        
        values = self.store[key]
        N = len(values)
        L = 0
        R = N-1
        resT = ("", -1)

        while L<=R:
            mid = (L+R)//2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                R = mid - 1
            else:
                L = mid + 1
                resT = (values[mid] if resT[1] <= values[mid][1] else resT)

        return resT[0]
