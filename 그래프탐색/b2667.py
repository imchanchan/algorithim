'''
[문제]:단지번호붙이기 // bfs/dfs
[day]: 25.04.12.
'''
from collections import deque
N = int(input())

buf = list(list(map(int,input())) for _ in range(N))

# print(buf)

dx = [0,0,-1,1]
dy = [-1,1,0,0]


visit = set()
re_cnt = []
cnt = 0

for i in range(len(buf)):
    for j in range(len(buf[0])):
        if buf[i][j] == 1 and (i,j) not in visit:
            
            cnt = 1

            q = deque()
            q.append([i,j])

            visit.add((i,j))

            while(q):
                
                x,y = q.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx<0 or ny<0 or nx>=len(buf) or ny>=len(buf[0]) :
                        continue

                    if buf[nx][ny]==1 and (nx,ny) not in visit:
                        cnt+=1

                        q.append([nx,ny])
                        visit.add((nx,ny))

            re_cnt.append(cnt)


print(len(re_cnt))
re_cnt.sort()
for i in re_cnt:
    print(i)
