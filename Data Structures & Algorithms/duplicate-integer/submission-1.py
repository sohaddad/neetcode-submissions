class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        countMap = {}
        for name in nums:
            # If countMap does not contain name
            if name not in countMap:
                countMap[name] = 1
            else:
                return True
        
        return False