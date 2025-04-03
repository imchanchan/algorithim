'''
[문제]:바이러스 / bfs
'''

from collections import deque

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
dx = [0, 0, 1, -1, 1, -1,-1,1]
dy = [1, -1, 0, 0, -1, 1,-1,1]
res = []
while(1):
    w, h = map(int, input().split())

    if w==0 and h==0:
        break

    else:
        graph=[]
        for _ in range(h):
            graph.append(list(map(int, input().split(' '))))

    q = deque()
    visit = set()
    cnt = 0

    for m in range(len(graph)):
        for n in range(len(graph[0])):
            if graph[m][n]==1 and (m,n) not in visit:

                q.append((m,n))
                
                while q:
                    x,y = q.popleft()

                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx<0 or ny<0 or nx>=len(graph) or ny>=len(graph[0]) or (nx,ny) in visit:
                            continue

                        if graph[nx][ny] == 1:
                            q.append((nx, ny))
                            visit.add((nx,ny))
                
                cnt+=1
    res.append(cnt)

for i in res:
    print(i)