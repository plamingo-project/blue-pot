# 14502 연구소(G4)
# 인생 첫 골드...

# 벽 세우기 -> 모든 정점 방문하며 벽 3개 짓기
# 3개가 되지 않은 경우 계속해서 벽을 짓는다.
# 3개인 경우에는 bfs를 통해 바이러스를 퍼트리고 안전지역 갯수를 구한다
# bfs -> 0인 모든 정점을 찾아 2로 변경함 (바이러스 퍼트리기), bfs가 끝나면 모든 정점을 탐색하며 0의 갯수 구한다

# 최댓값 -> bfs?
# 벽 3개를 세우는 모든 경우 따져보기
# 모든 0 중에 3개를 세우는 경우 찾기

# 1시간만 고민해보기


from collections import deque
from itertools import combinations as cm

import copy
import sys
input = sys.stdin.readline
# n * m (세로 * 가로) y < n / x < m

n, m = map(int, input().strip().split())

adj = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for _ in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

# print(adj)


def bfs(test_adj):
    # 방문 체크용 queue 생성
    queue = deque()

    for y in range(n):
        for x in range(m):
            if test_adj[y][x] == 2:
                queue.append((y, x))

    while queue:
        (cy, cx) = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            # 유효한 정점인지 확인
            if 0 <= ny < n and 0 <= nx < m:
                if test_adj[ny][nx] == 0:
                    # 바이러스 퍼트리기
                    test_adj[ny][nx] = 2
                    # 방문 처리
                    queue.append((ny, nx))

    # 탐색 끝난 경우
    global ret
    tmp = 0
    for y in range(n):
        for x in range(m):
            if test_adj[y][x] == 0:
                tmp += 1

    ret = max(ret, tmp)


# 메인 로직
# 최댓값
ret = 0
wall_candidates = []

# 벽 세울 수 있는 모든 조합 확인
for y in range(n):
    for x in range(m):
        if not adj[y][x]:
            wall_candidates.append((y, x))

for c in cm(wall_candidates, 3):
    test_adj = copy.deepcopy(adj)
    for y, x in c:
        test_adj[y][x] = 1

    bfs(test_adj)


print(ret)


# 조합으로 풀어보려다가 풀이를 참고했으나 알고보니 조합으로 푸는 것이 맞았다.
# 왜 재귀보다 조합이 더 시간복잡도가 낮게 나왔을까?
