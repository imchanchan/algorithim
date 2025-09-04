# 1️⃣ 입력 =================================================
N = int(input())
graph=[]
for i in range(N):
    graph.append(list(input().split(" ")))

# print(graph)


# 2️⃣ 함수 =================================================
#🔻 o; [조합공식] arr 안에서 r개 뽑는 방법법
def comb(arr, r, idx=0, path=None):
    """
    arr에서 r개를 선택하는 모든 조합을 반환하는 함수
    
    Args:
        arr: 선택할 원소들의 리스트
        r: 선택할 원소의 개수
        idx: 현재 선택할 수 있는 시작 인덱스
        path: 현재까지 선택된 원소들의 경로
    
    Returns:
        모든 조합의 리스트 (다중 리스트)
    """
    if path is None:
        path = []
    
    result = []  # 🔴결과를 저장할 리스트
    
    if len(path) == r:
        return [path[:]]  # 🔴현재 조합을 복사해서 반환
    
    for i in range(idx, len(arr)):
        path.append(arr[i])
        result.extend(comb(arr, r, i+1, path))  # 🔴재귀 결과를 확장
        path.pop()
    
    return result

# 🔻o; 그래프에서 (a,b)과 (b,a)의 합
def point_sum(a,b):
    # print('a', a, 'b', b)
    # print("point", f'= {int(graph[a][b])} + {int(graph[b][a])} = {int(graph[a][b])+int(graph[b][a])}')
    return int(graph[a][b]) + int(graph[b][a])


# #🔻 x ; [방법론1] 배열에서 두 원소를 선택해 뺀 값이 가장 작은 경우
# def find_min_difference(arr):
#     """
#     [방법론1]
#     배열에서 두 원소를 선택해서 뺀 값이 가장 작은 것을 찾는 함수
    
#     시간복잡도: O(n log n) - 정렬이 가장 비용이 큼
#     공간복잡도: O(1) - 추가 메모리 거의 없음
    
#     Args:
#         arr: 정수 배열
    
#     Returns:
#         (min_diff, num1, num2): 최소 차이값과 해당하는 두 원소
#     """
#     if len(arr) < 2:
#         return None, None, None
    
#     # 배열을 정렬 (O(n log n))
#     arr_sorted = sorted(arr)
    
#     min_diff = float('inf')
#     num1, num2 = None, None
    
#     # 인접한 원소들의 차이만 확인 (O(n))
#     for i in range(len(arr_sorted) - 1):
#         diff = arr_sorted[i + 1] - arr_sorted[i]
#         if diff < min_diff:
#             min_diff = diff
#             num1, num2 = arr_sorted[i], arr_sorted[i + 1]
    
#     return min_diff, num1, num2

# 🔻 x; [TABLE] : 2개 원소를 더하는게 table만들어서 연산하는것 보다 훨씬 편리하다.
# nC2_table = comb([i for i in range(0,N)],2)
# nC2_dict = {}  # 딕셔너리 생성

# 각 조합을 딕셔너리에 추가
# for combo in nC2_table:
#     key = combo  # [0, 1] 같은 형태
#     value = combo[0] + combo[1]  # 두 원소의 합
#     nC2_dict[tuple(key)] = value  # 리스트는 키로 사용할 수 없으므로 tuple로 변환

# # ===[딕셔너리 결과 확인]===
# # print("nC2 딕셔너리:")
# # for key, value in nC2_dict.items():
# #     print(f"{list(key)} -> {value}")



# 3️⃣ MAIN =================================================
'''
[해결과정]

1. 첫번째 - 해결한 부분 ✔️
## team => [0,1,2,3] 70개
## res  => 팀의 점수

2. 두번째 - 해결해야하는 포인트 ✔️
## r_team 구하기기 => team[0,1,2,3]의 반대팀 [4,5,6,7]

3. 세번째 - 해결해야하는 포인트 ✔️
## r_team에서 구한 팀은 team에서 구하지 않기 (중복연산 피하기기)

4. 네번째 - 메모리 문제
## teams을 모두 다 만들어놓고, 잘라서 해결했다... 문제가 되는 지점은 teams으로 만들어놓고, r_teams에서 또 만든다. 
'''

score = []
teams = comb(list(range(0,N)), int(N//2))
print('teams', teams)
teams = teams[:int(len(teams)//2)] # team과 r_team의 중복연산 피하기 

for team in teams:
    # r_team 구하기기
    r_team = []
    for i in range(0,N):
        if i not in team:
            r_team.append(i)

    # team의 점수
    point1 = 0
    for j in comb(team, 2):
        point1 += point_sum(j[0], j[1])
    # print(f'team = ', point1)

    # r_team의 점수
    point2 = 0
    for j in comb(r_team,2):
        point2 += point_sum(j[0], j[1])
    # print(f'r_team = ', point2)

    # 점수 계산
    score.append(abs(point1-point2))
    # print('socre = ',abs(point1 - point2))


# print('- - - - - -')

print(min(score))


# ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
'''
부딪힌 지점: 하나의 리스트에서 두개의 값을 뺐을때 최소값

- 1차 해결 
[방법론1] : 정렬 후 >> 인접한 값을 빼는 방법
[방법론2] : 모든 값을 직접 빼는 방법 

- 2차 해결
두 방법 모두 사용하지않고, 그때 그때 뺀 결과값을 score에 저장했다. 
'''


'''
부딫힌 지점: 팀을 나누는걸 조합으로 해결하는게 아니였어! 
(0,1,2,3) / (4,5,6,7)
이런식으로 나누었어야했는데

(0,1,2,3) / (1,2,3,4)
이렇게 나누게 되니, 한사람이 두팀에 들어가는 경우가 생겨버렸다. 

'''