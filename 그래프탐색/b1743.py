'''
[문제]:음식물 피하기 / bfs
'''

from collections import deque

n,m,k = map(int, input().split())

graph = [[0 for _ in range(m+1)] for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())

    graph[a][b] = 1

# print(graph)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()
visit = set()
res = []

for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j] == 1 and (i,j) not in visit:
            # print((i,j))
            q.append((i,j))
            visit.add((i,j))
            cnt = 0
            while q:
                x,y = q.popleft()
                cnt+=1
                # print(f"x,y {x, y}")

                for k in range(4):
                    # ** 중요 **

                    nx = x + dx[k]
                    ny = y + dy[k]
                    # print(f'nx,ny{nx, ny}')
                    if nx < 1 or ny<1 or nx>n or ny>m :
                        continue    
                    
                    if graph[nx][ny] == 1 and (nx,ny) not in visit:
                        # print(f'nx,ny {nx,ny}')
                        q.append((nx,ny))
                        visit.add((nx,ny))
            res.append(cnt)

print(max(res))



