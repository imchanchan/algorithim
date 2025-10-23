'''
[문제]: 미로만들기 // bfs/dfs
[day]: 25.10.22.
'''

from collections import deque
from os.path import pathsep

# ===== 0. 입력 =====
n = int(input())

rooms = []
for i in range(n):
    a = list(map(int, input().strip()))
    rooms.append(a)

for room in rooms:
    print(room)

# ===== 1. 탐색 =====
visited = [[0]*n for _ in range(n)]
paths = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y,path, cnt):
    print('** 1. 들어간다. ')
    # 락을 걸어준다. 
    if x == n-1 and y == n-1:
        print(f"** 4. 도달지점에 오신걸 환영합니다 : {path} ")
        paths.append((path[:],cnt)) # 복사해서, 경로저장
        print(path, '\n')
        return
    

    for k in range(4):
        # if (dx[k], dy[k]) != (1,0) and (dx[k], dy[k]) != (0,1):
        #     continue
        print(f"** 2. 사방을 살핀다. {k}")
        nx = x + dx[k]
        ny = y + dy[k]

        if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny] : ## 가지않을 조건 [1. 좌표이탈, 2. 방문한곳]
            continue

        if (nx, ny) in path:
            continue

        if rooms[nx][ny]== 0: ## 검정색일때, 카운팅
            cnt += 1
        
        # nx, ny 좌표 방문하기
        visited[nx][ny]=1
        # 경로별, 방문 좌표 저장하기
        print(f"** 3. {(nx, ny)}값이 path 배열{path}에 들어갑니다. ")
        path.append((nx, ny))

        dfs(nx,ny,path,cnt)

        # visited[nx][ny] = 0
        path.pop() # 백트래킹
        cnt -= 0

print(paths)

visited[0][0] = 1
dfs(0,0,[(0,0)],0)

print(paths)


'''
[생각1]
모든 길, 일단 지나가보기 => 지나가는 검정색을 카운팅하면 돼! => bfs보다 확실히, dfs가 좋다. 

bfs보다 dfs가 메모리적으로 좋다. 왜냐! 
1. 검정색이 한개만 나왔을 경우 최소값이기때문에, 다른 경로 탐색할 필요가 없어진다.
2. 항상, (1, n-1) 경로들중 최소값과, n 경로만 기억해두면된다. 



[dfs]
>> 백트래킹 사용한다. 

'''

'''
[문제1] : dfs 락을 걸어둔 (n-1, n-1) 좌표에서 끝나질 않는다.
[해결1] : visited = [[0]*n]*n 방문배열이 잘못됐다.
>> [[0]*n]*n => 얕은 복사 문제! 
        [0]*n -> [0,0,0] 이런 1차원 리스트를 만든다. 
        [0,0,0] 리스트 하나를 *n만큼 얕은복사한다. 

    >> 그러므로, 첫행 첫열 의값을 1로 수정하면, 같은 열에 있는 값이 모두 1이된다. 
        즉, [[1,0,0][1,0,0][1,0,0]]이 된다. 
    >> 모든 행이 같은 리스트 객체를 참조한다. 






'''