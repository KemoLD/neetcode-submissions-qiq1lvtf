class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []

        def search(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            elif total > target or i >= len(candidates):
                return
            else:
                curr.append(candidates[i])
                search(i + 1, curr, total + candidates[i])
                curr.pop()

                while i+1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                search(i + 1, curr, total )

        search(0, [], 0)
        return result
        