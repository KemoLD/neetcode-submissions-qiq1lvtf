class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        result = []

        for x in nums:
            count[x] = count.get(x, 0) + 1

        array = sorted(count.items(), key = lambda item: item[1], reverse = True)

        for i in range(k):
            result.append(array[i][0])


        return result
        