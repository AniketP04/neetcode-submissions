class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > target:
                right = middle
            else:
                left = middle + 1
        return left - 1 if (left - 1 >= 0 and nums[left - 1] == target) else -1