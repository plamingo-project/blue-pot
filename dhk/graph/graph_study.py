# python에서 인접 행렬로 graph 그리기
# graph = [[0 for _ in range(10)] for _ in range(10)]
# visited = [False for _ in range(10)]

# graph[1][2] = 1
# graph[2][1] = 1

# graph[1][3] = 1
# graph[3][1] = 1

# graph[3][4] = 1
# graph[4][3] = 1

# print(graph)
# print(visited)


# def go(graph, i, visited):
#     # 방문처리
#     visited[i] = True
#     print("Visit : ", i)
#     for j in graph[i]:
#         if (visited[j]):
#             continue
#         if j == 1:
#             go(graph, j, visited)


# for i in range(10):
#     for j in range(10):
#         if graph[i][j] == 1 and visited[i] == 0:
#             go(graph, i, visited)


# python에서 인접리스트로 그래프 활용
adj = [[] for _ in range(10)]
visited = [False for _ in range(10)]
# 간선 연결
adj[1].append(2)
adj[2].append(1)

adj[1].append(3)
adj[3].append(1)

adj[3].append(4)
adj[4].append(3)

print(adj)

# 정점 방문하는 함수


def go(i):
    visited[i] = True
    print("Visited: ", i)
    for j in adj[i]:
        if not visited[j]:
            go(j)


# 노드 0번부터 노드 찾고 dfs 수행
for a in range(10):
    if len(adj[a]) > 0 and not visited[a]:
        go(a)

# 그래프가 희소할 때는 인접리스트, 조밀할 때는 인접행렬 사용하기
