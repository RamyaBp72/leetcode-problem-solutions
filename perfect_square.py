class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = num ** 0.5
        temp = int(ans)
        return ans == temp