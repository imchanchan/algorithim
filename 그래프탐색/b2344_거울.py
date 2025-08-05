N, M = map(int, input().split(" "))


graph = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

graph_input = list(list(map(int, input().split(" "))) for _ in range(N))
print(graph_input)

for i in range(N):
    for j in range(M):
        graph[i + 1][j + 1] = graph_input[i][j]

print(graph)

# [1, N+1] : right
# [N+1, N+M+1]: up
# [N+M+1, 2*N+M+1]: left
# [2*N+M+1, 2*N+2*M+1]: down

# 0, 1, 2, 3
dir = ["right", "up", "left", "down"]

box = dict()
for i in range(1, 2 * N + 2 * M + 1):
    if 1 <= i < N + 1:
        box[i] = 0  # right
        graph[i][0] = i
        print(i)

    elif N + 1 <= i < N + M + 1:
        box[i] = 1  # up
        graph[N + 1][i - N] = i
        print(i)

    elif N + M + 1 <= i < 2 * N + M + 1:
        box[i] = 2  # left
        graph[N + 1 - (i - N - M)][M + 1] = i
        print(i)

    elif 2 * N + M + 1 <= i < 2 * N + 2 * M + 1:
        box[i] = 3  # down
        graph[0][M + 1 - (i - 2 * N - M)] = i
        print(i)

print(box)
print(graph)

# graph = list(list(map(int, (input().split(" ")))) for _ in range(N))

# print("box", box)
# print("reversed_box", reversed_box)
# print("graph", graph)


# from collections import deque

# q = deque()


# ###
# # [주의] : nx, ny에 대해서 범위에 대한 후처리 필요.
# ###
# def right(point):
#     x, y = point
#     if graph[x][y] == 0:
#         sign = "right"
#         nx = x + 1
#         ny = y
#         return sign, (nx, ny)
#     if graph[x][y] == 1:
#         sign = "up"
#         nx = x
#         ny = y - 1
#         return sign, (nx, ny)


# def left(point):
#     x, y = point
#     if graph[x][y] == 0:
#         sign = "left"
#         nx = x - 1
#         ny = y
#         return sign, (nx, ny)
#     if graph[x][y] == 1:
#         sign = "down"
#         nx = x
#         ny = y + 1
#         return sign, (nx, ny)


# def up(point):
#     x, y = point
#     if graph[x][y] == 0:
#         sign = "up"
#         nx = x
#         ny = y - 1
#         return sign, (nx, ny)
#     if graph[x][y] == 1:
#         sign = "right"
#         nx = x + 1
#         ny = y
#         return sign, (nx, ny)


# def down(point):
#     x, y = point
#     if graph[x][y] == 0:
#         sign = "down"
#         nx = x
#         ny = y + 1
#         return sign, (nx, ny)
#     if graph[x][y] == 1:
#         sign = "left"
#         nx = x - 1
#         ny = y
#         return sign, (nx, ny)


# for i in range(1, len(box + 1)):
#     q.append(box[i])

#     while q:
#         sign, point = q.popleft()

#         if sign == "right":
#             n_sign, (nx, ny) = right(sign, point)
#         if sign == "left":
#             n_sign, (nx, ny) = left(sign, point)
#         if sign == "up":
#             n_sign, (nx, ny) = up(sign, point)
#         if sign == "down":
#             n_sign, (nx, ny) = down(sign, point)

#         if 0 < nx <= N and 0 < ny <= M:
#             q.append(n_sign, (nx, ny))

#         # else:
# if sign == "right":
#     sign = "left"
# if sign == "left":
#     sign = "right"
# if sign == "up":
#     sign = "down"
# if sign == "down":
#     sign = "up"

# print(reversed_box[[sign, point]], end=" ")
