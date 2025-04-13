from collections import deque

N, M = map(int, input().split(' '))

q = deque()
visit = set()

q.append((N, 0))
visit.add(N)

while(q):
    cur_N, cur_t = q.popleft()

    if 0<=cur_N<=100_000:

        if cur_N+1 not in visit:
            # print('찬1')
            q.append((cur_N+1, cur_t+1))
            visit.add(cur_N+1)

        if cur_N-1 not in visit:
            # print('찬2')
            q.append((cur_N-1, cur_t+1))
            visit.add(cur_N-1)

        if cur_N*2 not in visit:
            # print('찬3')
            q.append((cur_N*2, cur_t+1))
            visit.add(cur_N*2)
    
    if cur_N == M:
        print(cur_t)
        break


