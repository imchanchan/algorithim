'''
[문제]: 점프 / dp 
'''

N = int(input())
map = list(list(map(int, input().split())) for _ in range(N))

dp = [[0 for _ in range(N)] for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j]>0 and map[i][j]!=0:
            if i+map[i][j]<N :
                dp[i+map[i][j]][j]+=dp[i][j]

            if j+map[i][j]<N :
                dp[i][j+map[i][j]]+=dp[i][j]

# print(dp)
print(dp[N-1][N-1])

