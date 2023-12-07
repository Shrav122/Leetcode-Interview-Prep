class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def dp(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dp(i + 1), dp(i + questions[i][1] + 1) + questions[i][0])
            return memo[i]

        n = len(questions)
        memo = [-1] * n
        return dp(0)