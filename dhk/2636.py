# 2636(G4) 치즈
# dfs 응용 문제인듯?
import sys
sys.setrecursionlimit(10**6)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 치즈가 있는 경우 상하좌우 모두 체크, 1이 아닌 경우 0으로 변경

# 내부 구멍인 경우도 고려를 해야함... 둘러쌓여있다면 사라지지 않는다


def dfs(y, x, visited):

    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        # 유효한 정점 확인
        if 0 <= ny < h and 0 <= nx < w:
            global adj
            if adj[ny][nx] == 0 and not visited[ny][nx]:
                dfs(ny, nx, visited)
            # 1인 경우
            if adj[ny][nx] == 1:
                adj[ny][nx] = 2
                visited[ny][nx] = True

    return


# 마지막 치즈 조각 갯수 => 메인 루프 돌 때마다 업데이트
ret = 0
# 그래프
adj = []
# 최종 걸린 시간 (메인 루프 횟수)
cnt = 0


# while문에서 치즈가 없어질 때까지 반복
# 매번 결과를 ret 값에 저장

# 그래프 구현
h, w = map(int, input().split())
for _ in range(h):
    row = list(map(int, input().split()))
    adj.append(row)

# print(adj)


while True:
    visited = [[False for _ in range(w)] for _ in range(h)]
    # 치즈가 있는지 계산
    tmp = 0
    for i in range(h):
        tmp += sum(adj[i])

    if tmp == 0:
        break
    else:
        ret = tmp

    # 메인 루프 횟수 증가
    cnt += 1

    dfs(0, 0, visited)

    # dfs 탐색 이후 녹일 치즈들 모두 녹이기
    for y in range(h):
        for x in range(w):
            if adj[y][x] == 2:
                adj[y][x] = 0

# 리턴
print(cnt, ret, sep="\n")
