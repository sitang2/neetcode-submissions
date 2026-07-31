class Solution:
    def climbStairs(self, n: int) -> int:
        #Check if n is less or equal to 2
        if n <= 2:
            return n
        #create a new array with 0 and len based on n 
        dp = [0] * (n + 1)
        #initalized the first 2 fix elements
        dp[1], dp[2] = 1, 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]