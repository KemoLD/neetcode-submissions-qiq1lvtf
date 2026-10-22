class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0

        while i < len(chars):
            chars[insert] = chars[i]
            insert += 1

            cnt = i
            while cnt < len(chars) and chars[i] == chars[cnt]:
                cnt += 1

            length = cnt - i
            if length > 1:
                for x in str(length):
                    chars[insert] = x
                    insert += 1
            
            i = cnt

        return insert