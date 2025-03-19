# 2583 영역 구하기(S1)
# m * n : x < n y < m

import sys

m, n, k = map(int, input().split())
sys.setrecursionlimit(10**6)

adj = [[0 for _ in range(n)] for _ in range(m)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


ret = []
cnt = 0


def dfs(y, x):
    global cnt
    adj[y][x] = 1
    cnt += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < m and 0 <= nx < n:
            if adj[ny][nx] == 0:
                dfs(ny, nx)
    return


for _ in range(k):
    x, y, tx, ty = map(int, input().split())
    for i in range(y, ty):
        for j in range(x, tx):
            adj[i][j] = 1

# print(adj)

for y in range(m):
    for x in range(n):
        if adj[y][x] == 0:
            # print(x, y)
            if cnt > 0:
                ret.append(cnt)
            cnt = 0
            dfs(y, x)

# 마지막 값 저장
ret.append(cnt)

print(len(ret))

for i in sorted(ret):
    print(i, end=" ")

# 왜 영역도 point
