# == [방향 정의] ==
# (0,1)  = right
# (0,-1) = left
# (1,0)  = up
# (-1,0) = down

# 0. 초기설정
N, M = map(int, input().split(' '))
graph = []
for _ in range(N):
    graph.append(list(input()))    
print(graph)

from collections import deque
R_end = 0 # Red 구멍 통과 
B_end = 0 # Blue 구멍 통과
visited = set()

# ===== 1. 초기 R 과 B point 찾기. =====
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            R_point = (i, j)
            cnt += 1
        if graph[i][j] == 'B':
            B_point = (i, j)
            cnt += 1
        
        # 두 point 모두 발견
        if cnt == 2:
            break
    # 두 point 모두 발견
    if cnt == 2:
        break

print(R_point, B_point)
visited.add(R_point)

# ===== 2. 초기 방향 설정 f_dir값 초기 방향 =====
# R 기준, 나아갈 방향 찾기 = 사방 훑기 (우선순위 'O' 먼저, 다음 '.')
x, y = R_point

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 이번 turn 방향 담기.
f_dir = deque()

for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]

    if graph[nx][ny] == 'O':
        R_end = 1
        break

    if graph[nx][ny] == '.':
        # 방향 확실하게 잡기
        ## (0,1) = right, (0,-1) = left, (1,0) = up, (-1,0) = down
        f_dir.append((dx[k], dy[k]))

# ===== 3. [re] 만들기 =====
# 조심할것 (B가 앞길을 가로막고있는 상황) : right & down : RB , left & up : BR 
dx, dy = f_dir.popleft()

re = ''

# 오른쪽 re == RB조심, 왼쪽 re == BR 조심
if (dx, dy) == (0,1) or (dx, dy) == (0,-1) :
    print('left or right')
    for u in range(N):
        if graph[nx][u] == '.' or graph[nx][u] == 'O':
            continue
        re += graph[nx][u]

# 아래 re == RB 조심, 위 re == BR 조심
if (dx, dy) == (1,0) or (dx, dy) == (-1,0) :
    print('down or up')
    for u in range(M):
        if graph[u][ny] == '.' or graph[u][ny] == 'O':
            continue
        re += graph[u][ny]



# ===== 4. 나아가기. =====
# (0) 나아가는 방법 [함수로 정의] : '#' 부딫힐때까지 나아가기
# (1) RB, BR 존재여부로, B와 R 중에 먼저 나아갈 것 결정하기.
# (2) 위에서, 정해진 순서에 맞게 나아가기. 

# ===== 4-0. =====
def go(point, visited, dir_x, dir_y): # 시작 지점, 방문 기록 표시, 해당 방향
    print(f'point = {point}, visited = {visited}, dir = ({dir_x, dir_y})')
    
    
    while 1:
        nx = point[0] + dir_x
        ny = point[1] + dir_y

        if nx<0 or nx>=N or ny<0 or ny>=M or (nx,ny) in visited:
            break

        if graph[nx][ny] == '#':
            break
        
        visited.add((nx, ny))
        point = (nx, ny)

    return point, visited
    
        




# ===== 4-1. =====
# (1) B 먼저 처리, 후에 R 처리
# (2) 각각 
if ((dx, dy) == (0,1) or (dx, dy) == (-1,0))  and "RB" in re :
    print('!', re)
    # B go
    # R go
    pass

if ((dx, dy) == (0,-1) or (dx, dy) == (1,0))  and "BR" in re :
    print('!', re)
    # B go
    # R go
    pass
    # B먼저 처리하기 => R 처리하기 


# ===== 4-2.  =====

print(f_dir)
# dx[k], dy[k] 방향으로 전진

print('&&', R_point)
point, visited = go(R_point, visited, dx, dy)
print('##최종 Point', point)
print('##최종 visited', visited)















# # 2. bfs 
# # 2-1. 방향은 R이 결정해.
# # 2-2. R이 움직일때, B도 같이 움직여.
# from collections import deque

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]

# q = deque()
# visited_R = set()
# visited_B = set()

# q.append([R_point, B_point])
# visited_R.add(R_point)
# visited_B.add(B_point)

# # while(q):
# #     (R_x, R_y), (B_x, B_y) = q.popleft()

# #     for k in range(4):
# #         # R 전진 
# #         R_nx = R_x + dx[k]
# #         R_ny = R_x + dy[k]
# #         if R_nx<0 or R_nx>=N or R_ny<0 or R_ny>=M or (R_nx, R_ny) in visited_R:
# #             continue()

# #         if graph[R_nx][R_ny] == '.':
# #             next_R_point = (R_nx, R_ny)
            
# #         if graph[R_nx][R_ny] == 'O':
# #             break

# #         # B 전진
# #         B_nx = B_x + dx[k]
# #         B_ny = B_y + dy[k]

# #         if B_nx<0 or B_nx>=N or B_ny<0 or B_ny>=M or (B_nx, B_ny) in visited_B:
# #             continue()

# #         if graph[B_nx][B_ny] == '.':
# #             next_B_point = (B_nx, B_ny)
        
# #         if graph[B_nx][R_ny]
# #             q.append([R_point, B_point])
# #             visited.add((nx, ny))


