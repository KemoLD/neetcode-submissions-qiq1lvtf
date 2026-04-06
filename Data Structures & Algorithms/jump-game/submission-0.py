class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxi = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= maxi:
                maxi = i

            
        return True if maxi == 0 else False
