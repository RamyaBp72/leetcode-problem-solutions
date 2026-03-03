class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        tempo, step = 1, 1
        while True:
            hours_needed = 0    
            
            for pile in piles:
                if pile % tempo == 0:
                    hours_needed += pile // tempo
                else:
                    hours_needed += pile // tempo + 1
            
            if hours_needed <= h:
                if step <= 10:
                    return tempo
                else:
                    tempo -= step // 10
                    step = max(1, step//100)
                    
            else:
                ratio = hours_needed // h 
                if ratio > 1:
                    tempo = tempo * ratio
                else:
                    tempo += step
                    step *= 10
        