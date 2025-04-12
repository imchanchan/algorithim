'''
[문제]:동물원 / dp
'''

N = int(input())

dp = [0,3,7]

# dp[3] = 2*dp[2]+dp[1]
# dp[1] = 2*dp[3]+dp[2] # dp[1] = dp[4]
# dp[2] = 2*dp[1]+dp[3] # dp[2] = dp[5]
# dp[3] = 2*dp[2]+dp[1] # dp[3] = dp[6]
# dp[1] = 2*dp[3]+dp[2] # dp[1] = dp[7]
# dp[2] = 2*dp[1]+dp[3] # dp[2] = dp[8]

for i in range(3, N+1):
    dp[i%3] =  2*dp[(i-1)%3] + dp[(i-2)%3] 

print(dp[N%3]%9901)