#INCOMPLETE SOLUTION - this considers robbing ALL alternative (odd OR even) houses only
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        dp[0] = nums[0]
        sum1 = dp[0]
        if n >= 2:
            dp[1] = nums[1]
            sum2 = dp[1]
        else:
            return sum1
            #or return dp[0]?
        for i in range(2, n):
            if i % 2 == 0:
                dp[i] = nums[i] + sum1
                sum1 = dp[i]
            else:
                dp[i] = nums[i] + sum2
                sum2 = dp[i]
        return max(dp[n-1], dp[n-2])
        #or return max(sum1, sum2)?

#TABULATION - WORKS SUCCESSFULLY
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_amt = {}
        #n = len(nums)
        max_amt[0] = nums[0]
        if len(nums) >= 2:
            max_amt[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                max_amt[i] = max(nums[i] + max_amt[i-2], max_amt[i-1]) 
        return max_amt[len(nums)-1]
#Note: Used 'len(nums)' everywhere instead of 'n' to try to decrease memory usage, but that didn't work.

#DONE