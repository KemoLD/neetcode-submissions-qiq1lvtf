class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num, exp):
            if num == 0:
                return 0
            if exp == 0:
                return 1

            res = helper(num * num, exp // 2)
            return num * res if exp % 2 else res

        result = helper(x, abs(n))
        if n >= 0:
            return result
        else:
            return 1/result