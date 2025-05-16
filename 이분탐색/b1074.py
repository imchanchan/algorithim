'''
[문제]:Z / 분할정복
- 분할정복이지만, .. 내가 풀고싶은대로 풀었다.. 
- res += 2**(2*k) * dic[m] 이 식으로 한방에 해결되는데..
'''


N, r, c = map(int, input().split(' '))

from collections import deque

q = deque()

row = 2**N
col = 2**N

# dic
dic = {(0,0):0, (1,0):1, (0,1):2, (1,1):3}



# 좌표 결정해보기.
for i in range(N):

    row = row//2
    col = col//2

    q.append((c//col, r//row))

    # print( i, "?", dic[(c//col, r//row)])

    r = r%row
    c = c%col
    
res=0
while q:
    k = len(q)-1
    m = q.popleft()

    res += 2**(2*k) * dic[m]
    # print(res)

print(res)
# print(q)


