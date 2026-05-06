class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak , current = 0, num
            while current in store:
                streak +=1
                current +=1
            res = max(res, streak)
        return res