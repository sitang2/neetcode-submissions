class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Given DISTINCT int numbers
        #Given target number.
        #Return a List of uniqure combination of numbers where the chosen numbers sum to target
        
        #Constraint:
            #numbers can be use multiple time
            
        res = []

        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res