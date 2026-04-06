class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        res = [amount+1] * (amount + 1)
        res[0] = 0

        for i in range(1, amount+1):
            for x in coins:
                if i >= x:
                    res[i] = min(res[i], 1 + res[i - x])

        return res[amount] if res[amount] != amount+1 else -1