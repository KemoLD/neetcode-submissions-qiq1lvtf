class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []

        def search(countOpen, countClose):
            if countOpen == countClose == n:
                s = ''.join(curr)
                result.append(s)
                return

            if countOpen < n:
                curr.append('(')
                search(countOpen +1, countClose)
                curr.pop()

            if countClose < countOpen:  
                curr.append(')')
                search(countOpen, countClose +1)
                curr.pop()  

        search(0,0)
        return result