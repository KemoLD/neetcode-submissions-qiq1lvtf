class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        copy = x
        reverse = 0

        while copy:
            digit = copy % 10
            copy = copy // 10

            reverse = (reverse * 10) + digit

        return reverse == x