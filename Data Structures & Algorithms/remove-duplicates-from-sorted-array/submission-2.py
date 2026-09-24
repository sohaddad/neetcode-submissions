class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        k = len(unique)
        nums[:len(unique)] = unique
        return k