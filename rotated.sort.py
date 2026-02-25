class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        low, high = 0, n - 1

        while low < high:
            mid = (low + high + 1) // 2
            if nums[mid] >= nums[0]:
                low = mid
            else:
                high = mid - 1

        border = low

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        if target >= nums[0]:
            return binary_search(0, border)
        else:
            return binary_search(border + 1, n - 1)