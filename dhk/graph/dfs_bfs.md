# DFS
깊이 우선 탐색

sudo code
```
DFS(u, adj)
u.visited = true
for each v ∈ adj[u]
if v.visited == false
DFS(v, adj)
```

1. 어떠한 정점 u를 방문처리하고 u에서 연결된 v지점을 탐색한다
2. 방문되어있지 않은 노드에 대해 재귀적으로 DFS를 호출한다

- 재귀 함수는 Stack으로 처리되기 때문에 DFS(가장 깊은 곳까지 방문) 역할을 수행할 수 있다.

- 좌표 주어지는 경우
```python
dy = [0, 0, 1, -1]  # y < n
dx = [1, -1, 0, 0]  # x < m


def dfs(x, y, adj):
    # 방문 처리 -> visited를 별도로 만들지 않아도 된다. 그냥 0으로 바꿔줘도 방문처리한 걸로 됨
    adj[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and adj[ny][nx] == 1:
            dfs(nx, ny, adj)
    return
```

# BFS
- 좌표 주어지는 경우
```python
    def bfs(adj, start_x, start_y, end_x, end_y):
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]
        queue = deque([(start_x, start_y, 1)])
        # 방문 처리
        adj[start_y][start_x] = 0

        while queue:
            (x, y, dist) = queue.popleft()

            if x == end_x and y == end_y:
                return dist

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < N and 0 <= nx < M and adj[ny][nx] == 1:
                    queue.append((nx, ny, dist + 1))
                    # 방문처리
                    adj[ny][nx] = 0
```
