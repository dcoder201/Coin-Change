class Solution:
    def count(self, coins, N, Sum):
        dp = [0] * (sum+1)
        dp[0] = 1
        for i in range(N):
          for j in range(coins[i], sum+1):
            dp[j] += dp[j-coins[i]]
            
        return dp[sum]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))
