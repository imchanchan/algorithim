# 2206	벽 부수고 이동하기
"""
6 4
0100
1110
1000
0000
0111
0000
"""
from collections import deque

N, M = map(int, input().split(" "))
graph = list(list(input()) for _ in range(N))
print(graph)


a_set = set([0, 0])
check = deque()
check.append((0, 0, 1))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


while check:
    x, y, cnt = check.popleft()
    print((x,y,cnt))

    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M or ((nx, ny) in a_set) or (graph[nx][ny]=='1'):
            continue
        print("append (x,y)", (nx, ny))
        check.append((nx, ny, cnt))
        a_set.add((nx, ny))

print(x, y)
print(a_set)
print(cnt-1)

# --------------------------------------------------------------------
'''

현재 ; 그래프탐색 완료
[문제1]
- 제거해야하는 1을 어떻게 맞춰야하는지 모르겠다. 

'''