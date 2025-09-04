# 입력
N, M= map(int, input().split(" "))
graph = []
graph.append([0 for _ in range(M+2)])
for _ in range(N):
    a = [0]
    a.extend(list(map(int, input().split(" "))))
    a.extend([0])
    graph.append(a)    
graph.append([0 for _ in range(M+2)])

# print(graph)


# (init) 초기 방향설정
direction = [0] 
direction.extend(["right"] * len(range(1, N+1)))
direction.extend(["up"] * len(range(N+1, M+N+1)))
# direction.extend(["left"] * len(range(M+N+2, 2*M+N+2)))
# direction.extend(["down"] * len(range(2*M+N+2, 2*M+2*N+2)))
# print(direction)

# 이동설정
direct_change = {"right" : "up",
        "up"    : "right",
        "left"  : "down",
        "down"  : "left"}

# (init) 위치설정

# ==== >> 1 ~ (N+M)/2
points = [0]
for i in range(1,N+1):
    points.append((i,1))
    ## (1,1), (2,1)

for i in range(1,M+1):
    points.append((N,i))
    ## (N, 1), (N, 2), (N, 3)

# ==== >> (N+M)/2+1 ~ N+M+1 : dict 
res_points = {}

cnt = N+M
for i in range(N,0,-1):
    cnt+=1
    res_points[(i, M+1)]= cnt

for i in range(M,0,-1):
    cnt+=1
    res_points[(0, i)] = cnt


# print(points)
# print(res_points)


# ----- ----- ----- ---
def direct_move(point):
    x, y = point
    
    if direct == "right":
        nx, ny = x, y+1
    elif direct == "left":
        nx, ny = x, y-1
    elif direct == "up":
        nx, ny = x-1,  y
    elif direct == "down":
        nx, ny = x+1, y

    return nx, ny

# ---- ---- ---- -----

result = [0 for _ in range(2*N+2*M)]
## ===== main =====
for i in range(1, N+M+1):

    direct = direction[i]
    point = points[i]
    x, y =point

    # 이동 후, 위치 재설정
    nx = x
    ny = y
    while(10000):
        # print("==== num ", i)
        # print('* 신호 ',graph[nx][ny])
        # print("* 현 위치 ", point)
        # print("* 현 방향 ", direct)

        # 1. 방향 설정
        if graph[nx][ny] == 1:
            direct = direct_change[direct]
            # if direct == "right":
            #     direct = "up"
            # elif direct == "left":
            #     direct = "down"
            # elif direct == "up":
            #     direct = "right"
            # elif direct == "down":
            #     direct = "left"
            # print("* 방향 바뀜 >> ", direct)
        ## graph[x][y] == 0 -> direct 그대로
        # print("* 방향 그대로")


        # 2. 방향 따라 이동
        nx, ny = direct_move(point)
        point = (nx, ny)
        # print("* 이동 >> ",(nx, ny))

        if nx<=0 or ny<=0 or nx>=N+1 or ny>=M+1:
            # x, y = point
            break


        
       
    # print(f"☑️  {i}일때, 도착 위치 {point} >> {res_points[(point)]}")
    result[i-1] = res_points[point]
    result[int(res_points[point])-1] = i

print(*result)



# -----------------------------------
'''
[1차 작업 실패] ==== 
첫번째 시도:
* graph = [0,1,0]
          [0,1,1]

* points = [0, (0, 0), (1, 0), (1, 0), (1, 1), (1, 2)]
* res_points = {(1, 2): 6, (0, 2): 8, (0, 1): 9, (0, 0): 10} >> dict으로 해결하기 어렵다. (0,2)=7, (0,2)=8 이기때문에!! 
 
[1차 개선] ==== 
graph = [0, *, *, *, 0]
        [*, 0, 1, 0, *]
        [*, 0, 1, 1, *]
        [0, *, *, *, 0]

start_points =  [0, (1, 1), (2, 1), (2, 1), (2, 2), (2, 3)]
res_points = {  (2,4):6, (1,4):7, (0,3):8, (0,2):9, (0,1):10 }
 
ex)
1일때, 도착 위치 (0, 2) >> 9

# 결과 switching 하는 방법
res[1] = 9
res[9] = 1
'''

'''
--------------------- >> 최종 출력값 << -------------------------
2 3
0 1 0
0 1 1
[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
[0, 'right', 'right', 'up', 'up', 'up']
[0, (1, 1), (2, 1), (2, 1), (2, 2), (2, 3)]
{(2, 4): 6, (1, 4): 7, (0, 3): 8, (0, 2): 9, (0, 1): 10}
==== num  1
* 신호  0
* 현 위치  (1, 1)
* 현 방향  right
* 방향 그대로
* 이동 >>  (1, 2)
==== num  1
* 신호  1
* 현 위치  (1, 2)
* 현 방향  right
* 방향 바뀜 >>  up
* 방향 그대로
* 이동 >>  (0, 2)
☑️  1일때, 도착 위치 (0, 2) >> 9
==== num  2
* 신호  0
* 현 위치  (2, 1)
* 현 방향  right
* 방향 그대로
* 이동 >>  (2, 2)
==== num  2
* 신호  1
* 현 위치  (2, 2)
* 현 방향  right
* 방향 바뀜 >>  up
* 방향 그대로
* 이동 >>  (1, 2)
==== num  2
* 신호  1
* 현 위치  (1, 2)
* 현 방향  up
* 방향 바뀜 >>  right
* 방향 그대로
* 이동 >>  (1, 3)
==== num  2
* 신호  0
* 현 위치  (1, 3)
* 현 방향  right
* 방향 그대로
* 이동 >>  (1, 4)
☑️  2일때, 도착 위치 (1, 4) >> 7
==== num  3
* 신호  0
* 현 위치  (2, 1)
* 현 방향  up
* 방향 그대로
* 이동 >>  (1, 1)
==== num  3
* 신호  0
* 현 위치  (1, 1)
* 현 방향  up
* 방향 그대로
* 이동 >>  (0, 1)
☑️  3일때, 도착 위치 (0, 1) >> 10
==== num  4
* 신호  1
* 현 위치  (2, 2)
* 현 방향  up
* 방향 바뀜 >>  right
* 방향 그대로
* 이동 >>  (2, 3)
==== num  4
* 신호  1
* 현 위치  (2, 3)
* 현 방향  right
* 방향 바뀜 >>  up
* 방향 그대로
* 이동 >>  (1, 3)
==== num  4
* 신호  0
* 현 위치  (1, 3)
* 현 방향  up
* 방향 그대로
* 이동 >>  (0, 3)
☑️  4일때, 도착 위치 (0, 3) >> 8
==== num  5
* 신호  1
* 현 위치  (2, 3)
* 현 방향  up
* 방향 바뀜 >>  right
* 방향 그대로
* 이동 >>  (2, 4)
☑️  5일때, 도착 위치 (2, 4) >> 6


9 7 10 8 6 5 2 4 1 3
'''