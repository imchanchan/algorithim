'''
[문제]: 알파벳/ dfs 백트래킹 + 비트마스크
'''

from collections import deque

def dfs(x, y, visited):

    global max_length 
    max_length = max(max_length,  sum(1 for v in visited.values() if v == 1))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=len(alp_graph) or ny<0 or ny>=len(alp_graph[0]):
            continue
        if visited[alp_graph[nx][ny]]==1 :
            continue

        visited[alp_graph[nx][ny]] = 1
        
        dfs(nx, ny, visited)

        visited[alp_graph[nx][ny]] = 0

# input
R,C = map(int, input().split(' '))
alp_graph = [list(input()) for _ in range(R)]


# solve
max_length = 0
visited = {i: 0 for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]}
visited[alp_graph[0][0]] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dfs( 0, 0, visited)

print(max_length)