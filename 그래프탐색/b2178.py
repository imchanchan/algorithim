from collections import deque

N, M = map(int, input().split(' '))
map = list(list(map(int, input())) for _ in range(N))

# print(map)

dx = [0,0,-1,1]
dy = [1,-1,0,0]


q = deque()
q.append((0,0,1))
visit = set((0,0))

while q:
    x, y, cnt = q.popleft()

    if x==len(map)-1 and y==len(map[0])-1:
        print(cnt)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=len(map) or ny<0 or ny>=len(map[0]):
            continue
        
        if (nx,ny) not in visit and map[nx][ny]==1:
            q.append((nx, ny, cnt+1))
            visit.add((nx,ny))
            # print((nx, ny))
    
    






