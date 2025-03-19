# 1012(S2) 유기농 배추
# 연결된 컴포넌트 문제

# dfs 수행 (why ? - 구현 쉬우니까 / also 최단거리 같은 거 아니니까 bfs 안써도됨)

# 1. 모든 정점 순회
# 2. 정점을 방문했었다면 -> continue
# 2-1. 아니면 dfs 실행 => dfs 실행할 때마다 ret +1

import sys

sys.setrecursionlimit(10**4)


dy = [0, 0, 1, -1]  # y < n
dx = [1, -1, 0, 0]  # x < m


def dfs(x, y, adj):
    adj[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and adj[ny][nx] == 1:
            dfs(nx, ny, adj)
    return


T = int(input())

for _ in range(T):
    ret = 0
    m, n, k = map(int, input().split())

    # n -> 세로 사이즈
    adj = [[0 for _ in range(m)] for _ in range(n)]

    # map 만들기
    for _ in range(k):
        x, y = map(int, input().split())
        adj[y][x] = 1

    # 모든 정점 방문 및 확인
    for y in range(n):
        for x in range(m):
            # 방문하지 않은 경우
            if adj[y][x] == 1:
                ret += 1
                dfs(x, y, adj)
    print(ret)
