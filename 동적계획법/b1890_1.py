'''
[문제]: 점프 / bfs
실패했다.. map의 크기가 커지면서 타임아웃 발생 !! -> dp로 풀어내야한다. 
'''

N = int(input())
map = list(list(map(int, input().split())) for _ in range(N))
dp = [[0 for _ in range(N)] for _ in range(N)]

from collections import deque

q = deque()
q.append((0,0))
dp[0][0]=1
visit=set()
cnt=0


while(q):
     
    x, y = q.popleft()

    if (x, y, cnt) not in visit:

        if x==N-1 and y==N-1:
            continue

        if x+map[x][y] < N and map[x][y]!=0:
            q.append((x+map[x][y], y))
            dp[x+map[x][y]][y] += 1
            visit.add((x,y,cnt))
        
        if 0< y+map[x][y] < N and map[x][y]!=0:
            q.append((x, y+map[x][y]))
            dp[x][y+map[x][y]] += 1
            visit.add((x,y,cnt))

print(dp)
print(dp[N-1][N-1])

   


    

