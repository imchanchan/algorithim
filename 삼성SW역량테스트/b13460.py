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
print(graph)

from collections import deque
R_end = 0 # Red 구멍 통과 
B_end = 0 # Blue 구멍 통과
visited = set()

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



# 대 함 수 시작 !! 
#  input : 이동 시작 point, visited 
#  실행(one-cycle) : 1. 방향찾기, 2. re확인 , 3. 나아가기
#  ouput : 이동 완료 point, visited

find_O = False

def cycle(point):
    global visited
    global find_O

    # ===== [ 1. 초기 방향 설정 f_dir값 초기 방향 ]  =====
    # R 기준, 나아갈 방향 찾기 = 사방 훑기 (우선순위 'O' 먼저, 다음 '.')
    x, y = point

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    # 이번 turn 방향 담기.
    f_dir = deque()


    out = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if graph[nx][ny] == 'O' and (nx, ny) not in visited:
            f_dir.append((dx[k], dy[k]))
            R_end = 1
            find_O = 1
            return "find it."

        if graph[nx][ny] == '.' and (nx, ny) not in visited:
            # 방향 확실하게 잡기
            ## (0,1) = right, (0,-1) = left, (1,0) = up, (-1,0) = down
            f_dir.append((dx[k], dy[k]))

        else :
            out += 1        
    if out == 4:
        return "사방이 모두 막혀있어, 나아갈 곳이 없습니다."


    # ===== [ 2. [re] 만들기 ] =====
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



    # =====[ 3. 나아가기. ]=====
    # (0) 나아가는 방법 [함수로 정의] : '#' 부딫힐때까지 나아가기
    # (1) RB, BR 존재여부로, B와 R 중에 먼저 나아갈 것 결정하기.
    # (2) 위에서, 정해진 순서에 맞게 나아가기. 

    # ===== 3-0. =====
    def go(point, visited, dir_x, dir_y): # 시작 지점, 방문 기록 표시, 해당 방향
        global find_O

        print(f'point = {point}, visited = {visited}, 방향 = ({dir_x, dir_y})')
        
        
        while 1:
            nx = point[0] + dir_x
            ny = point[1] + dir_y

            if graph[nx][ny] == 'O':
                find_O = 1

            if nx<0 or nx>=N or ny<0 or ny>=M or (nx,ny) in visited:
                break

            if graph[nx][ny] == '#':
                break
            

            visited.add((nx, ny))
            point = (nx, ny)

        return point, visited
        

    # ===== 3-1. =====
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


    # ===== 3-2.  =====


    print(f_dir)
    # dx[k], dy[k] 방향으로 전진

    print('&&', point)
    point, visited = go(point, visited, dx, dy)

    print('##최종 Point', point)
    print('##최종 visited', *visited)

    if find_O == 1:
        return 'find it'

    return point

# for i in range(5):
#     print(f"==={i}===")
#     point = cycle(R_point)
#     R_point = point
#     print("리얼", point)

i=0
while 1:
    
    print(f"---{i}---")
    point = cycle(R_point)
    R_point = point 
    print("리얼", point)

    if point == 'find it':
        i+=1
        break
    if point == "사방이 모두 막혀있어, 나아갈 곳이 없습니다.":
        break
    i+=1

print('find_O',find_O)
print("res", i)

print('##', point)
print('##', visited)



'''
[문제1]
>> 예상했다. bfs로 접근해야하는데, 일단 여러갈래가 나오지 않는 상태에서 테스트 해본거였기 때문에, 예제 3에서는 통과했고,
예제 4, 6에서 갈래가 두개로 나뉘는 순간, 에러 발생! bfs 써야하는 이유 => [예제 4, 6]

[해결1]
>> go를 bfs로 바꿔야한다. 
즉, "방향을 찾는다. 그대로 나아간다."는 틀림.

>> 방향을 찾고, 나아가는걸 bfs로,, 이게 느낌은 아는데 설명이 안된다.

>> 싹 다시 풀어버리자. b13460_bfs.py 파일로 이동 ~

'''