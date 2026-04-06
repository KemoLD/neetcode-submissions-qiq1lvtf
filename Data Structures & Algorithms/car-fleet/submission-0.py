class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        pair.sort(reverse= True)

        prevEnd = (target - pair[0][0]) / pair[0][1]
        fleets = 1

        for p,s in pair[1:]:
            x = (target - p) / s 
            if x <= prevEnd:
                continue
            else:
                fleets += 1
                prevEnd = x

        return fleets

                 