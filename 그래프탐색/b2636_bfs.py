from collections import deque
'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''
# --------
# input
N, M = map(int, input().split(" "))

graph = []
outside = []

cnt_total = 0
for i in range(N):
    s = list(map(int, input().split(" ")))
    graph.append(s)
    cnt_total += sum(s)

    outside.append([0 for _ in range(M)])


import copy

def melt(graph, outside):
    graph_copy = copy.deepcopy(graph)
    outside_copy = copy.deepcopy(outside)

    q = deque()
    visit = set()

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]


    q.append((0,0))
    visit.add((0,0))
    outside[0][0] = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx<0 or nx>=N or ny<0 or ny>=M or (nx,ny) in visit:
                continue
            if graph_copy[nx][ny] == 0:
                q.append((nx, ny))
                visit.add((nx, ny))

                outside[nx][ny] = 1
    
            else:
                graph_copy[nx][ny] = 2


    total_1 = 0 
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j] == 2:
                graph_copy[i][j]= 0
        total_1 += sum(graph_copy[i])
    
    # print("toatl ;", total_1)
                        
    return graph_copy, outside, total_1



cnt = 0 
res = 0





while (1):
    graph1, outside1, total_1 = melt(graph, outside)
    graph = copy.deepcopy(graph1)
    outside = copy.deepcopy(outside1)
    # print(total_1)

    # print("="*10)
    # for g1 in graph1:
    #     print(g1)

    cnt += 1

    if total_1==0:
        break

    res = total_1

if cnt == 1:
    print(cnt)
    print(cnt_total)

else:
    print(cnt)
    print(res)
    



'''
[문제1]
graph1, outside1 = melt(graph, outside)
graph2, outside2 = melt(graph1, outside1)

각각의 객체를 비교해보면,
print(graph1 is graph2)    >> True
print(outside is outside1) >> True
모두 True로 반환된다. 

"" 이런 문제를 in-place 라고한다!! ""


[해결1]
함수 내부에서 깊은 복사로 사용해, input 행렬과 output 행렬의 객체를 분리하는 작업을 진행했다! 

13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
3
5

>> 성공!! 


[문제2]
제출했는데, 틀렸다. 

반례를 찾았다. 
5 5
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0

처음 시작시, 1 카운트를 했어야한다. 

[해결2]
# == 초기 1 카운팅팅
for s in graph:
    cnt_total += sum(s)
# print(cnt_total)
>> main부분에서 처음그냥 싹 더했는데
>> input으로 입력할때마다, cnt_total을 세어야겠다. 굳이 for문 한번더 쓰지말고! 
'''