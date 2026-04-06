class Solution:
    def numDecodings(self, s: str) -> int:
        
        def decode(index):

            if index >= len(s):
                return 1
            if s[index] == '0':
                return 0


            x = decode(index+1)
            if (index+1) < len(s) and (s[index] == '1' or (s[index] == '2' and s[index+1] in '0123456')):
                x += decode(index+2)

            return x

        return decode(0)