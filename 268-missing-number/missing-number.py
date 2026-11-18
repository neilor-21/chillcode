class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        num_set = set(nums)
        return next(i for i in range(0, n + 1) if i not in num_set)