'''
[문제]:토마토 / bfs
'''
from collections import deque


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(M)]
visit = set()
dq = deque()


dx = [+1,-1,0,0]
dy = [0,0,+1,-1]



# print(arr)

for i in range(M):
    for j in range(N):
            if arr[i][j] == 1:
                visit.add((i,j))
                dq.append([i,j,0])

while(dq):
    print(dq)

    x,y,cnt = dq.popleft() 
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # ** 중요 **
        if nx < 0 or ny<0 or nx>=M or ny>=N :
            continue
        
        if arr[nx][ny] == 0 and (nx,ny) not in visit:
            dq.append([nx,ny,cnt])
            visit.add((nx,ny))
            arr[nx][ny] += 1

c = 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            print(-1)
            c+=1
            break
if c==0:
    print(cnt-1)


# 1을 찾는다. []
# 4방을 훑어보고, 1로 바꾼다. (cnt+=1)
# 더이상 0이 없어지면, 전체적으로 0이 남아있는지 확인한다. -> 앞으로 땡겨서 생각해보자.
# if 0이 있다면, -1
#        없다면, cnt

