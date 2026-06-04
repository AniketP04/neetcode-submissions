class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        first_index = -1

        while low <= high:
            mid = (low+high)//2
            count = sum(1 for num in nums if num <= mid)
            if count > mid:
                first_index = mid
                high = mid -1
            else:
                low = mid + 1
        return first_index