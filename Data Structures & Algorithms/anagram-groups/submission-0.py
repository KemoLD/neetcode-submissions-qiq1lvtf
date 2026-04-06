class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key in count:
                count[key].append(word)
            else:
                count[key] = [word]

        return count.values()