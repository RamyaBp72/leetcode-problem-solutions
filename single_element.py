class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            if count == 1:
                return num
        return -1 