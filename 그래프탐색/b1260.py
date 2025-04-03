'''
[문제] DFS와 BFS / bsf,dfs
'''

from collections import deque

n,m,s = map(int, input().split())
graph = {i : [] for i in range(1,n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start_node):
    stack = [start_node]
    visit = set()

    while stack:
        a = stack.pop()
        if a in visit:
            continue
        print(a, end=' ')
        visit.add(a)

        # print(sorted(graph[a], reverse=True))
        for child in sorted(graph[a], reverse=True):
            if child not in visit:
                stack.append(child)


def bfs(start_node):
    q = deque()
    q.append(start_node)
    visit = set()

    while q:
        a = q.popleft()
        print(a, end=' ')

        visit.add(a)


        for i in sorted(graph[a], reverse=False):
            if i not in visit:
                q.append(i)
                visit.add(i)
            
dfs(s)
print()
bfs(s)