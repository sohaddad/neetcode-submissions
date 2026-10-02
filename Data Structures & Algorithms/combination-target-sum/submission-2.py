class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        counter = 0
        res = []
        subset = []

        def dfs(i, counter):
            if counter == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or counter > target:
                return
            subset.append(nums[i])
            counter += nums[i]
            dfs(i, counter)
            subset.pop()
            counter -= nums[i]
            dfs(i + 1, counter)

        dfs(0, counter)
        return res