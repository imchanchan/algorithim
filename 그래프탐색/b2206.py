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
# print(graph)


visited = set()
visited.add((0,0,0))
check = deque()
check.append((0, 0, 1, 0)) # x, y, cnt, distory(1파괴 여부)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result_sign = 0
num = 0
res = []
while check:
    num+=1
    x, y, cnt, distory = check.popleft()

    if x == N-1 and y == M-1:
        result_sign = 1
        print(cnt)
        break
    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue


        # 1. 빈칸이면, gogo!! 
        if graph[nx][ny]=='0' and (nx, ny, distory) not in visited:
            visited.add((nx, ny, distory))
            check.append((nx, ny, cnt+1, distory))

        # 2. distory가 0인데, check_cell이 1이라면, 즉, 벽이 한번도 부서진적이 없었다면, 부수고 들어가기!! 
        elif graph[nx][ny] == '1' and distory == 0 and (nx, ny, 1) not in visited:
            visited.add((nx, ny, 1))
            check.append((nx, ny, cnt+1, 1))


    
if result_sign == 0:
    print(-1)


# --------------------------------------------------------------------
'''
현재 ; 그래프탐색 완료

1. [문제]
- 제거해야하는 1을 어떻게 맞춰야하는지 모르겠다. 

[대책1]
>> 완전탐색 ? -> X
>> 전략 : 그냥 처음 1을 만나면, 부실 수 있게 만들면 돼. 굳이 그다음이 0인지는 내가 고민할 게 아니야. BFS가 알아서 해결할 문제지. 
성공이다!!!!!!!!!! 

--

2. [문제]
4 4
0111
1111
1111
1110

이 예시에서 
(0, 0, 1, 0)
deque([])
append (x,y) (0, 1)
(0, 1, 2, 1)
deque([])
append (x,y) (0, 0)
(0, 0, 3, 1)
deque([])
0 0
{0, (0, 0), (0, 1)}
3
>> 결과가 3 나왔다. 


[해결2]
출력값에서 마지막 q에 들어갔던 값의 x, y를 확인해서 [N-1, M-1]값인지 확인하면 된다. 



---

채점 결과 ; "틀렸습니다."

3. [문제]
>> if distory==0 and graph[x][y]=='1':
    distory = 1
    graph[x][y] ='0'
    print("111")
이 과정에서 graph[x][y]=='0' 으로 설정해놓으면, 
다음 경로 탐색에서도 그대로 유지되어 문제가 생긴다. 

예제같은 경우는 [0,0]에서 [N-1, M-1]까지 갈때 경로가,
1개 밖에 없어서 문제가 발생하지 않았지만
정답까지 향하는 경로가 여러개일때 문제가 생길 수 있다!! 

[해결]
>> if graph[x][y]=='0':
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M or ((nx, ny) in a_set):
                continue


            # print("append (x,y)", (nx, ny))
            check.append((nx, ny, cnt, distory))
            a_set.add((nx, ny))

이부분에 들어가기위해 graph[x][y] == '0'을 위해서 해줬기 때문에,
graph[x][y] =='0' 을 if문 끝나고 해준다. 

* graph를 복제해서 체크할까도 생각했지만, 메모리 문제를 생각했을때 해당부분만 돌려놓으면되지
  graph 전체를 기억하고 있을 필요가 없었다. 


채점 결과 ;  "틀렸습니다."

4. [문제]
>> a_set = set((0, 0, 0))은 {0}이 된다. 
>> set에서 방문을 기록할때 (x,y,distory=0)과 (x,y, distory=1)은 다른 상태이다. 
이점을 간과하고 (x,y)좌표로만 방문여부를 확인했다. 

[해결]
깔끔하게 다시 짰다. 

- 고려할점1 : visited.add((x,y,distory))에서 (x,y,0)과 (x,y,1)은 각각 다른 상태이다.   
- 고려할점2 : graph[x][y]는 상태 확인만하고, 직접 바꾸지 말기! (위험해.)
             파괴 여부는 distory한테 맡겨!! 
" 성공했습니다~~ !! "

'''