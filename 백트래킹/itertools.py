import itertools

# 예시 원소 리스트와 뽑을 개수 r
data = [1, 2, 3]
r = 2

# 1) 조합 (Combinations) – 순서 없이 r개 선택
comb = list(itertools.combinations(data, r))
print("조합 (combinations):", comb)
# 출력: [(1, 2), (1, 3), (2, 3)]

# 2) 순열 (Permutations) – 순서 있게 r개 선택
perm = list(itertools.permutations(data, r))
print("순열 (permutations):", perm)
# 출력: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 3) 중복 조합 (Combinations with replacement) – 중복을 허용하고 순서 없이 r개 선택
comb_wr = list(itertools.combinations_with_replacement(data, r))
print("중복 조합 (combinations_with_replacement):", comb_wr)
# 출력: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# 4) 중복 순열 (Cartesian product) – 중복을 허용하고 순서 있게 r개 선택
prod = list(itertools.product(data, repeat=r))
print("중복 순열 (product):", prod)
# 출력: [(1, 1), (1, 2), (1, 3),
#        (2, 1), (2, 2), (2, 3),
#        (3, 1), (3, 2), (3, 3)]
