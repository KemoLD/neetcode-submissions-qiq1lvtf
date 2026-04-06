class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0

        for x in s:
            if x == '(':
                leftMin = leftMin + 1
                leftMax = leftMax + 1
            elif x == ')':
                leftMin = leftMin - 1
                leftMax = leftMax - 1
            else:
                leftMin = leftMin - 1
                leftMax = leftMax + 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0
