'''
[문제]:기타리스트 / bfs
'''

N, S, M = map(int, input().split())  # 갯수, 시작, 무게
val = list(map(int, input().split()))

from collections import deque

q = deque()
q.append((S,0))
visit = set()
visit.add((S,0))
ans = -1

while q:
    a, i = q.popleft()

    if 0<=i<len(val):
        if 0<=a+val[i]<=M and (a+val[i], i+1) not in visit:
            q.append((a+val[i], i+1))
            visit.add((a+val[i], i+1))
        if 0<=a-val[i]<=M and (a-val[i], i+1) not in visit:
            q.append((a-val[i], i+1))
            visit.add((a-val[i], i+1))

    else :
        ans = max(a,ans)

print(ans)