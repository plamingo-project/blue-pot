# 1926 - 그림(S1)

from collections import deque


def bfs(y, x):
    global cnt
    queue = deque([(y, x)])
    adj[y][x] = 0
    cnt += 1

    while queue:
        (cy, cx) = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            # 유효한 정점
            if 0 <= ny < n and 0 <= nx < m:
                if adj[ny][nx] == 1:
                    queue.append((ny, nx))
                    cnt += 1
                    adj[ny][nx] = 0

                    # do bfs
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, m = map(int, input().split())
adj = []

for _ in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

ret = 0
cnt = 0
nums = 0

for y in range(n):
    for x in range(m):
        if adj[y][x] == 1:
            nums += 1
            cnt = 0
            bfs(y, x)
            ret = max(ret, cnt)

print(nums, ret, sep="\n")
