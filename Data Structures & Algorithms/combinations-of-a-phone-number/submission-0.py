class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def search(index, currS):
            if len(currS) == len(digits):
                result.append(currS)
                return

            for x in digitToChar[digits[index]]:
                search(index + 1, currS + x)

        if digits:
            search(0, "")

        return result