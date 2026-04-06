class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        def sumOfsquares(x):
            sum = 0

            while x:
                y = x % 10
                y = y ** 2
                sum += y
                x = x //10

            return sum

        while n not in visit:
            visit.add(n)
            n = sumOfsquares(n)

            if n ==1:
                return True

        return False

        

