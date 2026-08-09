class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        n = len(nums)
        mid = (n + 1) // 2
        small = arr[:mid][::-1]
        large = arr[mid:][::-1]
        nums[::2] = small
        nums[1::2] = large 