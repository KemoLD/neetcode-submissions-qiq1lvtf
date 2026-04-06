class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])

        left = 0
        right = len(values) -1

        res = ''
        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid -1


        return res
        
