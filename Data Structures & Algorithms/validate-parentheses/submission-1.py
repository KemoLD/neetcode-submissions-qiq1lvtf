class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for x in s:
            if x == '(':
                stack.append(')')
            elif x == '[':
                stack.append(']')
            elif x == '{':
                stack.append('}')
            else:

                if not stack or x != stack.pop():
                    return False

        return not stack
        