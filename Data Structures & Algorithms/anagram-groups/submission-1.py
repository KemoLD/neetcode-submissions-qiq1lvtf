class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = {}

        for word in strs:

            c = [0] * 26

            for i in word:
                c[ord(i) - ord('a')] += 1
            key = tuple(c)

            if key in count:
                count[key].append(word)
            else:
                count[key] = [word]

        return count.values()