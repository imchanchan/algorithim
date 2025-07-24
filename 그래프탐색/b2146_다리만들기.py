N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [-1,1,0,0]

from collections import deque

q = deque()
s = set()
group_s = set()

cnt = 0
for x in range(len(graph)):
    for y in range(len(graph[0])):

        # 각 덩어리의 초기 좌표 
        if graph[x][y] == 1 and (x,y) not in s:
            cnt += 1

            q.append((x,y,cnt))
            s.add((x,y))
            group_s.add((x,y,cnt))

            # 각 덩어리 순회
            while(q):
                x, y, cnt = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx<0 or nx>=len(graph) or ny<0 or ny>=len(graph[0]) or (nx, ny) in s:
                        continue

                    if graph[nx][ny]==1:
                        q.append((nx, ny, cnt))
                        s.add((nx,ny))
                        group_s.add((nx,ny,cnt))

                    

group_s = list(group_s)  # set → list

mini = float('inf')  # 충분히 큰 수로 초기화

q.append(group_s[0])

for i in range(len(group_s)):
    for j in range(i + 1, len(group_s)):
        xi, yi, gi = group_s[i]
        xj, yj, gj = group_s[j]

        if gi != gj:
            dist = abs(xi - xj) + abs(yi - yj)
            if dist > 0:
                mini = min(mini, dist - 1)

print(mini)
