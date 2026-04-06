class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda x: x[0])
        res = [intervals[0]]

        for i,j in intervals[1:]:
            if i <= res[len(res)-1][1]:
                res[len(res)-1][1] = max(j, res[len(res)-1][1])
            else:
                res.append([i,j])

        return res