class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}

        for x in strs:
            indices = [0] * 26
            for i in x:
                indices[ord(i) - ord('a')]+= 1

            key = tuple(indices)
            if key in result:
                result[key].append(x)
            else:
                result[key] = [x]

        return list(result.values())