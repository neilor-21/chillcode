class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maj = {}
        for num in nums:
            if num in maj:
                maj[num] += 1
            else:
                maj[num] = 1
        return max(maj, key = maj.get)