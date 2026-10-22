class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0

        while i < len(chars):
            groupLen = 1
            while i + groupLen < len(chars) and chars[i] == chars[i + groupLen]:
                groupLen += 1

            chars[insert] = chars[i]
            insert += 1
            if groupLen > 1:
                string = str(groupLen)
                chars[insert : insert + len(string)] = list(string)
                insert += len(string)

            i +=  groupLen

        return insert