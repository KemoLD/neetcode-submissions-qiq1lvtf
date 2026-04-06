class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == '+':
                x = stack.pop() +  stack.pop()
                stack.append(x)
            elif s == '*':
                x = stack.pop() *  stack.pop()
                stack.append(x)
            elif s == '-':
                one = stack.pop()
                two = stack.pop() 
                x = two - one
                stack.append(x)
            elif s == '/':
                one = stack.pop()
                two = stack.pop() 
                x = int((float(two) / one))
                stack.append(x)
            else:
                stack.append(int(s))

        return stack[-1]