# 2178(S1) - 미로 탐색
# 최단거리 => BFS
# N * M 배열 (미로)

from collections import deque

# x, y, dist 저장하기 (queue)
# start => (x,y,dist)

# 시간초과 발생


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


N, M = map(int, input().split())
adj = [[] for _ in range(N)]


for i in range(N):
    tmp = []
    row = input()
    for c in row:
        adj[i].append(int(c))

# bfs + 최솟값 (정점마다 이동할 때 가중치 더하기)
print(bfs(adj, 0, 0, M-1, N-1))

# 미로 탐색 시 별도로 visited 두지 않고 지나온 길을 벽으로 만들면 됨
