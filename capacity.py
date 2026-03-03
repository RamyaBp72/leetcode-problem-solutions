class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def total_days(capacity):
            day = 0
            running_sum = 0
            for weight in weights:
                if running_sum + weight > capacity:
                    day += 1
                    running_sum = weight
                else:
                    running_sum += weight
            day = day + 1 if running_sum > 0 else day
            return day
            
        left = max(weights)
        right = sum(weights)
        while left < right:
            middle = (left + right) // 2
            if total_days(middle) <= days:
                right = middle
            else:
                left = middle + 1
        return left