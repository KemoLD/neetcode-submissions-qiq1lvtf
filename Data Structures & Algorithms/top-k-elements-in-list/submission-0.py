class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1

        array = [ [] for _ in range(len(nums) + 1)]

        for i,j in count.items():
            array[j].append(i)

        result = []

        for i in range(len(array) -1, -1, -1):
            for x in array[i]:
                result.append(x)
                if len(result) == k:
                    return result

        return result
        