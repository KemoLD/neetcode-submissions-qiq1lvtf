class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = defaultdict(int)
        res = 0
        curr = 0
        l = 0

        for i in range(len(fruits)):
            cnt[fruits[i]] += 1
            curr += 1

            while len(cnt) > 2:
                cnt[fruits[l]] -= 1
                curr -= 1
                if not cnt[fruits[l]]:
                    del cnt[fruits[l]]
                l += 1

            res = max(res, curr)

        return res