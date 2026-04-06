class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]

        left = 0
        right = len(nums) -1

        while(left <= right):
            if nums[left] < nums[right]:
                mini = min(mini, nums[left])
                break

            mid = (right + left) //2
            mini = min(mini, nums[mid])

            if nums[left] <= nums[mid]:
                left = mid+1
            else:
                right = mid -1 
                
        return mini