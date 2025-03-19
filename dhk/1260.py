# 1260 - BFS와 DFS
from collections import deque

N, M, V = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 작은 번호부터 방문하도록 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS 구현


def dfs(graph, i, visited):
    # 방문처리
    visited[i] = True
    # 방문 후 동작 수행
    print(i, end=" ")
    # 정점 i에 연결된 정점 확인
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j, visited)


# def dfs(graph, i, visited):
#     visited[i] = True
#     print(i, end=' ')
#     for j in graph[i]:
#         if not visited[j]:
#             dfs(graph, j, visited)

# BFS 구현


def bfs(graph, i, visited):
    queue = deque([i])
    # i - 시작 지점
    visited[i] = True  # 큐에 넣을 때 방문 처리

    while queue:
        value = queue.popleft()
        # queue에서 꺼내며 특정 동작 수행
        print(value, end=" ")

        for j in graph[value]:
            if not visited[j]:  # 방문하지 않은 노드만 추가
                queue.append(j)
                visited[j] = True  # 큐에 넣을 때 방문 처리


# 방문 체크 배열
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

# DFS 실행
dfs(graph, V, visited_dfs)
print()
# BFS 실행
bfs(graph, V, visited_bfs)
