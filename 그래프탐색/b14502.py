'''
[문제]:연구소 / bfs + 조합
'''
import copy
from collections import deque

## 함수1: 조합론 / 0인 값을 기준으로 3개 인덱스값 뽑아내기 위함.
def dfs(s, n, m, buf,n_buf):

    for i in range(s, n+1):
        if len(buf)==m:
            n_buf.append(buf[:])  # 현재 buf를 복사해서 저장
            return 

        if i not in buf:
            buf.append(i)     
            dfs(i,n,m,buf,n_buf)
            buf.pop()

## 함수2: map 안에 있는 val값의 인덱스를 visit에 넣는다. 즉, len(visit)은 val값의 개수다.
def bfs(visit, val, map):

    q = deque()

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for i in range(N):
        for j in range(M):

            if map[i][j] == val and (i,j) not in visit:
                q.append((i,j))
                visit.append((i,j))
            
                while(q):
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx<0 or nx>=N or ny<0 or ny>=M:
                            continue

                        if map[nx][ny]==val and (nx,ny) not in visit:
                            q.append((nx,ny))
                            visit.append((nx,ny))

# 함수3: map을 기준으로 2를 찾고, 바이러스를 퍼트린후 바이러스의 갯수를 반환한다. 
def bfs2(map):

    q = deque()
    visit = list()

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    cnt=0

    for i in range(N):
        for j in range(M):

            if map[i][j] == 2 and (i,j) not in visit:
                q.append((i,j))
                visit.append((i,j))

                cnt += 1
            
                while(q):
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx<0 or nx>=N or ny<0 or ny>=M:
                            continue

                        if map[nx][ny]==0 and (nx,ny) not in visit:
                            q.append((nx,ny))
                            visit.append((nx,ny))
                            cnt+=1
    return cnt
                
                                 
# ==== [실행코드] ====
                                   
N, M = map(int, input().split(' '))
map = list(list(map(int, input().split(' '))) for _ in range(N))


## 1. 좌표에 0인 모든 좌표값을 넣어준다.
visit=[]
bfs(visit, 0, map)


## 2. 모든 0의 점의 총 3가지 조합 쌍 구하기 (index 관점)
n_buf = []
dfs(1,len(visit), 3, [], n_buf)

min_bfs2=[] ## [4에서 사용]


## 3. 해당 조합의 종류로 벽(0->1)을 만들어서, copy_map 완성하기
for xyz in n_buf: 

    copy_map = copy.deepcopy(map) # 복사

    x, y, z = xyz # 벽세워야하는 인덱스

    i,j = visit[x]

    # 벽세우기
    copy_map[visit[x-1][0]][visit[x-1][1]] = 1
    copy_map[visit[y-1][0]][visit[y-1][1]] = 1
    copy_map[visit[z-1][0]][visit[z-1][1]] = 1
    
    ## 4. 벽이 생긴 copy_map기준으로, 바이러스 퍼트린 후 바이러스 갯수를 min_bfs2에 넣는다.
    min_bfs2.append(bfs2(copy_map))

## 5. 최종답 : (전체갯수) - (바이러스 퍼진후, 바이러스 갯수의 최소값) - (초기 벽의 갯수+3)
visit_1=[]
bfs(visit_1,1,map) # 1의 갯수 파악하기 = len(visit_1)

print( (N*M) - min(min_bfs2) - (len(visit_1)+3) )
