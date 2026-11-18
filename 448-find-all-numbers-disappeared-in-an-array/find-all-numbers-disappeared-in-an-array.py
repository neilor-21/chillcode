class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        num_set = set(nums)
        none = [i for i in range(1, n + 1) if i not in num_set]
        return none   