class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        s = sorted(count.items(), key = lambda i: i[1], reverse = True)
        print(s)

        for i in range(k):
            res.append(s[i][0])

        return res