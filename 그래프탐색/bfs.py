'''
bfs 연습용
'''

from collections import deque

arr = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	
m = len(arr)
n = len(arr[0])


dx = [+1,-1,0,0]
dy = [0,0,+1,-1]

visit = set() # 점으로 들어감.

cnt = 0
ans = 0

dq= deque()

visit.add((0,0))
dq.append([0,0,0])

while dq :

    x, y, cnt = dq.popleft()
    cnt += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # ** 중요 **
        if nx < 0 or ny<0 or nx>=m or ny>=n :
            continue

        if (nx,ny) not in visit and arr[nx][ny]== 1 :

            visit.add((nx,ny))
            dq.append([nx,ny, cnt])

            if nx == n-1 and ny == n-1:
                ans = cnt

if ans == 0 :
    print(-1)
else :
    print(cnt)

