class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = list(dict.fromkeys(nums))
        return len(nums)