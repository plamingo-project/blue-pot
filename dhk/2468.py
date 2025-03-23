# 2468 안전 영역(S1)
# 아무 지역도 물에 잠기지 않을 수도 있다. -> h == 0인 경우도 고려해야한다.

import sys

sys.setrecursionlimit(10**6)
n = int(input())

# print(n)
adj = []
# max h
mh = 1

# return value
ret = 1

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x, adj, size, current_h, visited):
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            if adj[ny][nx] - current_h > 0:
                if not visited[ny][nx]:
                    dfs(ny, nx, adj, size, current_h, visited)
    return


for _ in range(n):
    row = list(map(int, input().split()))
    mh = max(mh, max(row))
    # print(row)
    adj.append(row)

# print(mh)
# print(adj)

# 높이마다 loop 실행 (시나리오)
for h in range(1, mh+1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    # ret 초기화
    cnt = 0
    # 현재 높이 h 기준으로 컴포넌트 갯수 구하기 (안전지역 갯수)
    for y in range(n):
        for x in range(n):
            # 안전지대
            if adj[y][x] - h > 0:
                if not visited[y][x]:
                    cnt += 1
                    dfs(y, x, adj, n, h, visited)

    ret = max(ret, cnt)

print(ret)
