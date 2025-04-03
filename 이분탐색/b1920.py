'''
[문제]:수찾기 / 이분탐색
'''

N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
b_list = list(map(int, input().split()))

for target in b_list:
    left, right = 0, len(arr) - 1
    found = False

    while left <= right:
        mid = left + (right-left) // 2

        if arr[mid] == target:
            found = True
            break
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # print(f'left,{left}')
    
    if found:
        print(1)
    else:
        print(0)



# 이분탐색 알고리즘 쓰지 않고, 무작정 풀었던 코드 -> 시간초과. 망했팡.
# N = int(input())
# a_list = sorted(list(map(int, input().split(' '))))

# M = int(input())
# b_list = list(map(int, input().split(' ')))

# for i in b_list:
#     if i < a_list[int(N/2)]:
#         if i in a_list[:int(N/2)]:
#             print(1)

#         else:
#             print(0)

#     else: 
#         if i in a_list[int(N/2):]:
#             print(1)
#         else:
#             print(0)

