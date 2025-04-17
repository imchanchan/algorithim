'''
itertool없이 날것으로 구현
'''


# [순열 (Permutation)]
# arr에서 r개를 "중복없이 순서고려" 뽑는 경우의수
# 단, arr = [1,2,3,4] 같은 수가 없는 배열
def perm(arr, r, used=[], path=[]):
    if len(path) == r:
        print(path)
        return
    for i in range(len(arr)):
        if i in used:
            continue
        path.append(arr[i])
        used.append(i)
        perm(arr, r, used, path)
        used.pop()
        path.pop()

perm([1, 2, 3], 2)

print('- - - - -')

 
# [조합 (Combination)]
# arr에서 r개를 "중복없이 순서no고려" 뽑는 경우의수
# 단, arr = [1,2,3,4] 같은 수가 없는 배열
def comb(arr, r, idx=0, path=[]):
    if len(path) == r:
        print(path)
        return
    for i in range(idx, len(arr)):
        path.append(arr[i])
        comb(arr, r, i+1, path)
        path.pop()

comb([1, 2, 3], 2)

print('- - - - -')


# [중복순열 (Permutation)]
# arr에서 r개를 "중복해서 순서고려" 뽑는 경우의수
# 단, arr = [1,2,3,4] 같은 수가 없는 배열
def repeat_perm(arr, r, path=[]):
    if len(path) == r:
        print(path)
        return
    for i in range(len(arr)):
        path.append(arr[i])
        repeat_perm(arr, r, path)
        path.pop()

repeat_perm([1,2,3,4], 2)

print('- - - - -')


# [순열 (Permutation)]
# arr에서 r개를 "중복없이 순서고려" 뽑는 경우의수
# 단, arr = [1,2,3,4] 같은 수가 없는 배열
def repeat_comb(arr, r, idx=0, path=[]):
    if len(path) == r:
        print(path)
        return
    for i in range(idx, len(arr)):
        path.append(arr[i])
        repeat_comb(arr, r, i, path)  # i부터 시작! (중복 허용)
        path.pop()

repeat_comb([1, 2, 3], 2)
