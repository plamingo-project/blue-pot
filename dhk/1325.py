# 1325(S1) 효율적인 해킹
from collections import deque
import sys

input = sys.stdin.readline


def bfs(start):
    # 방문 처리
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        # 현재 확인 정점
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                # 방문 처리
                visited[next] = True
                queue.append(next)
                count += 1
    return count


# 입력
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 단방향: b → a
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

# bfs로 최대 감염 수 구하기
max_hack = -1
result = []

# 1번 컴퓨터부터 탐색
for i in range(1, n + 1):
    # 감염 갯수 -> bfs에서 리턴
    hacked = bfs(i)
    if hacked > max_hack:
        max_hack = hacked
        result = [i]
    elif hacked == max_hack:
        result.append(i)

print(*result)
