class Solution(object):
    def numTilings(self, n):
        MOD = 1000000007
        if n<=2:
            return n
        if n==0:
            return 1

        dp = [0]*(n+1)
        dp[0]= 1
        dp[1]= 1
        dp[2]= 2
        for i in range(3,n+1):
            dp[i]= (2*dp[i-1]+dp[i-3])%MOD

        return dp[n]
        
