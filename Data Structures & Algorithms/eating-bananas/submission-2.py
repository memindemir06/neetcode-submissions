class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        piles.sort()

        left = 1
        right = piles[-1]

        minSpeed = right

        while left <= right:
            k = left + ((right - left) // 2)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                minSpeed = min(minSpeed, k)
                right = k - 1
            else:
                left = k + 1
        
        return minSpeed


