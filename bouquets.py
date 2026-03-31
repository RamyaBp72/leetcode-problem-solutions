class Solution:
    def minDays(self, bloomDay, m, k):
        
        if m * k > len(bloomDay):
            return -1

        def canMake(day):   # ✅ FIXED INDENT
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            
            if canMake(mid):
                right = mid
            else:
                left = mid + 1

        return left