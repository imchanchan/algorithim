# == [방향 정의] ==
# (0,1)  = right
# (0,-1) = left
# (-1,0)  = up
# (1,0) = down

# ===== 0. 초기설정 ===== 
N, M = map(int, input().split(' '))
graph = []
for _ in range(N):
    graph.append(list(input()))    

from collections import deque
R_end = 0 # Red 구멍 통과 
B_end = 0 # Blue 구멍 통과
visited = set()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# ===== 1. 초기 R 과 B point 찾기. =====
R_point = 0
B_point = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            R_point = (i, j)

        if graph[i][j] == 'B':
            B_point = (i, j)

        
        # 두 point 모두 발견
        if R_point != 0 and B_point != 0 :
            break
    # 두 point 모두 발견
    if R_point != 0 and B_point != 0 :
        break

print(R_point, B_point)
visited.add(R_point)
for g in graph:
    print(g)


from collections import deque
q = deque()
q.append((R_point))

while q:
    x, y = q.popleft()

    for k in range(4):
        x = dx[k]
