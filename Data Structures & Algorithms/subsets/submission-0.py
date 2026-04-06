class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def search(index, curr):
            if index >= len(nums):
                result.append(curr.copy())
                return

            curr.append(nums[index])
            search(index + 1, curr)

            curr.pop()
            search(index + 1, curr)

        search(0, [])
        return result