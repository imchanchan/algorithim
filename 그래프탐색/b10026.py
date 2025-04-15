from collections import deque


def bfs(map):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    visit = set()
    cnt = 0

    for i in range(n):
        for j in range(n):
            if (i,j) not in visit:
                
                q.append((i,j))
                visit.add((i,j))
                cnt+=1

                while(q):
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue

                        if map[nx][ny]==map[x][y] and (nx,ny) not in visit: 
                            q.append((nx,ny))
                            visit.add((nx,ny))
    return cnt
                        
n = int(input())
map = list(list(input()) for _ in range(n))

import copy
n_map = copy.deepcopy(map)
for i in range(n):
    for j in range(n):
        if map[i][j]=='G':
            n_map[i][j]='R'

print(bfs(map), end=' ')
print(bfs(n_map))

