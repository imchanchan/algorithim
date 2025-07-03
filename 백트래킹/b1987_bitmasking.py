'''
[문제]: 알파벳/ dfs 비트마스크
'''

from collections import deque
max_length = 0
def dfs(x, y, bitmask, cnt):

    global max_length 
    max_length = max(max_length, cnt)


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=len(alp_graph) or ny<0 or ny>=len(alp_graph[0]):
            continue
        
        idx = ord(alp_graph[nx][ny]) - ord('A')
        

        ## [틀림1] : bitmask에 &연산(00=0, 01=0, 10=0, 11=1)을 취해서 중복확인한다.
        # if bitmask>>idx == 1:  
        #     continue
        if bitmask & (1 << idx): # 중복확인
            continue


        ## [틀림2] : 방문체크를 한 값은 bitmask값은 다음 dfs함수에서 받아드리는 bitmask값이야. 즉, 백트래킹이 없는거랑 연결지어 생각해봐.
        # bitmask |= 1<<idx # 방문체크
        # print(bin(bitmask))
        # dfs(nx, ny, bitmask, cnt+1)
        dfs(nx, ny, bitmask | (1 << idx), cnt + 1)


        ## [틀림3] : set, list(mutable)와 다르게 bitmask는 int(immutable)하기 때문에 백트래킹 필요없음!!
        ## mutable  은 dfs함수에 같은 변수, 같은 주소값을 보내고, (깊은 복사)
        ## immutable은 dfs함수에 같은 변수, 다른 주소값을 보낸다. (얕은 복사)
        # bitmask |= bin(1<<idx) -> 필요없음

# input
R,C = map(int, input().split(' '))
alp_graph = [list(input()) for _ in range(R)]

'''
[접근] : 딕셔너리26개 key를 문자열 00000000..00 20개로 생각하자.
A = 0b00000...001
B = 0b00000...010
ABC = 0b0000...111

이렇게 중복확인하기. 
'''

# [첫번쨰 값 방문체크]
start_idx = ord(alp_graph[0][0]) - ord('A') # ord = 문자 → 아스키코드
# print(start_idx)
bitmask = (1 << start_idx)
# print(bin(bitmask))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt = 1
dfs( 0, 0, bitmask, cnt)
print(max_length)

