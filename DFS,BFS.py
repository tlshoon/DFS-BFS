# 스택
# 후입선출
# stack = []
#
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()
#
# print(stack)
# print(stack[::-1])

# 큐
# 선입선출
# from collections import  deque
#
# queue = deque()
#
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()
#
# print(queue)
# queue.reverse()
# print(queue)

# 재귀함수
# def recursive_function():
#     print("재귀 함수를 호출합니다.")
#     recursive_function()
#
# recursive_function()
#
# 재귀함수 종료
# def recursive_function(i):
#     if i == 100:
#         return
#     print(i, "번째 재귀 함수에서", i+1, "번째 재귀 함수를 호출합니다.")
#     recursive_function(i+1)
#     print(i, "번째 재귀 함수를 종료합니다.")
# recursive_function(1)

# 인접행렬
'''INF = 999999999

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)'''

# 인접리스트
'''graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))

print(graph)'''

# DFS 예제
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
#
# visited = [False] * 9
#
# dfs(graph, 1, visited)

# BFS 예제
# from collections import deque
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#
#     visited[start] = True
#
#     while queue:
#         v = queue.popleft()
#         print(v, end = ' ')
#
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
#
# visited = [False] * 9
#
# bfs(graph, 1, visited)

# 음료수 얼려 먹기
# n,m = map(int,input().split())
#
# ice_board = []
# for i in range(n):
#     ice_board.append(list(map(int,input())))
#
# count = 0
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def dfs(start_x, start_y):
#     ice_board[start_x][start_y] = 1
#
#     for i in range(4):
#
#         nx = start_x + dx[i]
#         ny = start_y + dy[i]
#
#         if(nx >= 0 and nx < n and ny >= 0 and ny < m):
#             if(ice_board[nx][ny] == 0):
#                 dfs(nx,ny)
#
#
# for i in range(n):
#     for j in range(m):
#         if (ice_board[i][j] == 0):
#             dfs(i,j)
#             count += 1
#
# print(count)


# 미로탈출
# from collections import deque
#
# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# check = [[0]*m for _ in range(n)]  # 방문 기록용 2차원 리스트
#
# count = [[0]*m for _ in range(n)]  # 이동칸 기록용 2차원 리스트
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def bfs():
#     queue = deque()
#     queue.append((0,0))
#     check[0][0] = 1
#     count[0][0] = 1
#
#     while queue:
#         x,y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if (nx >=0 and nx < n and ny >=0 and ny < m):
#
#                 if(check[nx][ny] == 0 and graph[nx][ny] == 1):  # 인접한 노드를 방문할 수 있는지 확인
#
#                     queue.append((nx,ny))
#                     check[nx][ny] = 1
#                     count[nx][ny] = count[x][y] + 1
#
#     return count[n-1][m-1]
#
# print(bfs())
