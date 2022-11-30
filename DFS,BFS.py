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

#음료수 얼려 먹기
# n,m = map(int,input().split())
#
# ice_board = []
# for i in range(n):
#     ice_board.append(list(map(int,input())))
#
# dx = [0,0,-1,1]   # 상하좌우 진행용 방향 리스트
# dy = [-1,1,0,0]
#
# count = 0  # 아이스크림 개수
#
#
# def dfs(start_x,start_y):
#
#     ice_board[start_x][start_y] = 1  # 현재 노드를 방문 처리
#
#     for i in range(4):  # 현재 노드와 인접한 노드 모든 노드들을 탐색하며, 방문 가능할 경우 방문
#         nx = start_x + dx[i]  # 인접 노드 좌표
#         ny = start_y + dy[i]
#
#         if (nx >=0 and nx < n and ny >= 0 and ny < m):  # 인접 노드가 얼음판 내부에 위치할 경우
#             if(ice_board[nx][ny] == 0):  # 입접 노드에 음료수를 채울 수 있는지 확인
#                 dfs(nx,ny)  # 인접 노드 방문
#
#
# for i in range(n):
#     for j in range(m):
#         if (ice_board[i][j] == 0):  # 해당 노드에 음료수를 채울 수 있다면
#             dfs(i,j) # 해당 노드에 dfs 탐색 시작
#             count += 1
# print(count)

# 음료수 얼려먹기 다른 풀이
# n,m = map(int,input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
#
#
# def dfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >=m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         return True
#     return False
#
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             print(i,j)
#             result += 1
# print(result)


# 미로탈출
# from collections import deque
#
# n,m = map(int,input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# dx = [-1,1,0,0]   # 이동할 네 방향 정의(상,하,좌,우)
# dy = [0,0,-1,1]
#
#
# def bfs(x,y):
#     queue = deque()  # 큐 구현을 위해 deque 라이브러리 사용
#     queue.append((x,y))
#     while queue:  # 큐가 빌 때까지 반복
#         x,y = queue.popleft()
#         for i in range(4):  # 현재 위치에서 네 방향으로의 위치 확인
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:  # 벽인 경우 무시
#                 continue
#             if graph[nx][ny] == 1:  # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx,ny))
#     return graph[n-1][m-1]
#
# print(bfs(0,0))

# dfs 풀이
# n, m = map(int,input().split())
# graph = [list(map(int,input())) for _ in range(n)]
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def dfs(x,y):
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx and nx < n and 0 <= ny and ny < m:
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 dfs(nx,ny)
#
#     return graph[n-1][m-1]
#
# print(dfs(0,0))

######################## 3장 문제 ########################
# 특정 거리의 도시 찾기
# from collections import deque
#
# n,m,k,x = map(int,input().split())
# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#
# distance = [-1] * (n+1)  # 모든 도시에 대한 최단 거리 초기화
# distance[x] = 0
#
# q = deque([x])
# while q:
#     now = q.popleft()
#     for next_node in graph[now]:  # 현재 도시에서 이동할 수 있는 모든 도시를 확인
#         if distance[next_node] == -1:  # 아직 방문하지 않은 도시라면
#             distance[next_node] = distance[now] + 1
#             q.append(next_node)
#
# check = False
# for i in range(1,n+1):
#     if distance[i] == k:
#         print(i)
#         check = True
#
# if check == False:
#     print(-1)

#  연구소
# n,m = map(int,input().split())
# data = []
# temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트
#
# for _ in range(n):
#     data.append(list(map(int,input().split())))
#
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# result = 0
#
# # DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
#
# def virus(x,y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 상,하,좌,우 중에서 바이러스가 퍼질 수 있는 경우
#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2
#                 virus(nx,ny)
#
# # 현재 맵에서 안전 영역의 크기 계산하는 메서드
# def get_score():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score
#
# # DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
# def dfs(count):
#     global result
#     # 울타리가 세 개 설치된 경우
#     if count == 3:
#         for i in range(n):
#             for j in result(m):
#                 temp[i][j] = data[i][j]
#         # 각 바이러스의 위치에서 전파 진행
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(x,y)
#         # 안전 영역의 최댓값 계산
#         result = max(result,get_score())
#         return
#     # 빈 공간에 울타리 설치
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1
#
# dfs(0)
# print(result)
