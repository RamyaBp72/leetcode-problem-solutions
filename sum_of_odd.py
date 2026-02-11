class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i in range(n):
            total_subarrays = (i + 1) * (n - i)
            odd_count = (total_subarrays + 1) // 2
            total += arr[i] * odd_count
        return total