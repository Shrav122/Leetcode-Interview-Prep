class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        dp=[[-1 for j in range(m+1)] for i in range(n+1)] #Shifting the indexes
        for i in range(n+1):
            dp[i][0]=1
        for j in range(1,m+1): # we are starting it from 1 because for j<1 we have to return 1
            dp[0][j]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][m]