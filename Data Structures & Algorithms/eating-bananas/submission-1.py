import math as math

class Solution:
    def EatingScore(self, piles, h, k) -> int:
        time_spent = 0
        for amount in piles:
            time_spent += math.ceil(amount / k)
        if time_spent <= h:
            return 1
        else:
            return -1

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        current_min = high

        while low <= high:
            mid = (low + high) // 2

            if self.EatingScore(piles, h, mid) > 0:
                high = mid - 1
                if mid < current_min:
                    current_min = mid
            else:
                low = mid + 1
        
        return current_min

