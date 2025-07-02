'''
[문제]: 알파벳/ dfs 백트래킹
'''

from collections import deque

# input
R,C = map(int, input().split(' '))
alp_graph = [list(input()) for _ in range(R)]


def dfs(q,check_alp):
    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=len(alp_graph) or ny<0 or ny>=len(alp_graph[0]):
                continue
            if alp_graph[nx][ny] in check_alp:
                continue

            q.append([nx, ny, cnt+1])
            check_alp.append(alp_graph[nx][ny])
            print("q", q)
            print("check_alp", check_alp)

            dfs(q, check_alp)

            res.append(len(check_alp))
            check_alp.pop()

# solve
q = deque()
q.append([0,0,0]) # x, y, cnt

check_alp = list()
check_alp.append(alp_graph[0][0])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

res = []
dfs(q, check_alp)

print(max(res))