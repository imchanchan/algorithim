'''
[문제]: 알파벳/ dfs 백트래킹
'''

from collections import deque

# input
R,C = map(int, input().split(' '))
alp_graph = [list(input()) for _ in range(R)]

max_length = 0

def dfs(x, y, check_alp):

    global max_length 
    max_length = max(max_length, len(check_alp))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=len(alp_graph) or ny<0 or ny>=len(alp_graph[0]):
            continue
        if alp_graph[nx][ny] in check_alp:
            continue

        check_alp.add(alp_graph[nx][ny])
        # print("check_alp", check_alp)

        dfs(nx, ny, check_alp)

        check_alp.remove(alp_graph[nx][ny])

# solve

check_alp = set()
check_alp.add(alp_graph[0][0])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dfs( 0, 0, check_alp)

print(max_length)