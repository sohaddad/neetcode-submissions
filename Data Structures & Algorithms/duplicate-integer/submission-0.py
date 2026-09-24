class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = sorted(set(nums))
        if len(unique) == len(nums):
            return False
        return True