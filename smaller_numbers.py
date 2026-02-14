class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_s = sorted(nums)
        output = []
        for i in nums:
            output.append(nums_s.index(i))
        return output