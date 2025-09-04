# 입력
N, M= map(int, input().split(" "))
graph = []
for _ in range(2):
    graph.append(list(map(int, input().split(" "))))
print(graph)

# (init) 초기 방향설정
direction = [0] 
direction.extend(["right"] * len(range(1, M+1)))
direction.extend(["up"] * len(range(M+1, M+N+1)))
direction.extend(["left"] * len(range(M+N+1, 2*M+N+1)))
direction.extend(["down"] * len(range(2*M+N+1, 2*M+2*N+1)))
print(direction)

# 이동설정
move = {"right" : "up",
        "up"    : "right",
        "left"  : "down",
        "down"  : "left"}

# (init) 위치설정
points = [0]
for i in range(0,N):
    points.append((i,0))

for i in range(0,M):
    points.append((N-1,i))

res_points = {}

cnt = N+M
for i in range(N-1,-1,-1):
    res_points[(i, M-1)]= cnt

for i in range(M-1,-1,-1):
    cnt+=1
    res_points[(0, i)] = cnt


print(points)
print(res_points)





# ----- ----- ----- ---
def right(point):
    x, y = point
    return (x, y+1)

def left(point):
    x, y = point
    return (x, y-1)

def up(point):
    x, y = point
    return (x-1,  y)

def down(point):
    x, y = point
    return (x+1, y)

# ---- ---- ---- -----

for i in range(1, N+M+1):

    direct = direction[i]
    point = points[i]
    x, y =point

    # 이동 후, 위치 재설정
    nx = x
    ny = y
    while(1):
        print('graph',graph[nx][ny])
        print("*", point)
        print("*이전", direct)

        # 1. 방향 설정
        if graph[nx][ny] == 1:
            if direct == "right":
                direct = "up"
            elif direct == "left":
                direct = "down"
            elif direct == "up":
                direct = "right"
            elif direct == "down":
                direct = "left"
            print("*이후", direct)
        ## graph[x][y] == 0 -> direct 그대로



        # 2. 방향 따라 이동
        if direct == "right":
            nx, ny = right(point)
        if direct == "left":
            nx, ny = left(point)
        if direct == "up":
            nx, ny = up(point)
        if direct == "down":
            nx, ny = down(point)

        if nx<0 or ny<0 or nx>=N or ny>=M:
            # x, y = point
            break

        # 3. 위치 이동
        point = (nx, ny)
        
       
    print(f"{i}일때, 위치 point {point}")

    print(f"{point} >> {res_points[(point)]}")





# -----------------------------------
'''
[1차 작업 실패]
첫번째 시도:
* graph = [0,1,0]
          [0,1,1]

* points = [0, (0, 0), (1, 0), (1, 0), (1, 1), (1, 2)]
* res_points = {(1, 2): 6, (0, 2): 8, (0, 1): 9, (0, 0): 10} >> dict으로 해결하기 어렵다. (0,2)=7, (0,2)=8 이기때문에!! 
 
[1차 개선]
graph = [0, *, *, *, 0]
        [*, 0, 1, 0, *]
        [*, 0, 1, 1, *]
        [0, *, *, *, 0]

start_points =  [0, (1, 1), (2, 1), (2, 1), (2, 2), (2, 3)]
res_points = {  (2,4):6, (1,4):7, (0,3):8, (0,2):9, (0,1):10 }
 

# switching 하는 방법
res[1] = 9
res[9] = 1



'''