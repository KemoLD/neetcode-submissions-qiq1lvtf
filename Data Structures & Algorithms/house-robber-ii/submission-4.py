class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]
            
            
        def calc(houses):

            if len(houses) < 1:
                return 0
            elif len(houses) < 2:
                return houses[0]
            

            x = [0] * len(houses)
            x[0] = houses[0]
            x[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                x[i] = max( houses[i] + x[i-2], x[i-1])

            return x[len(houses)-1]

        return max(calc(nums[1:]), calc(nums[:-1]))
        