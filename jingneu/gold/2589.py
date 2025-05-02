import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

#상하좌우 이웃한 육지로만 가능 
#보물 - 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳

#start 정해서 - 가장 멀리 갈 수 있는 거리로 이동(bfs) -> 최댓값 갱신
#위에서 방문했으면 넘어감

N, M = map(int, input().split(" "))
arr = [list(input()) for _ in range(N)]

# visited = [[False]*M]*N <- 얕은 복사, 이렇게 하면 안됨
# visited = [[False]*M for _ in range(N)]  # 각 행이 독립된 리스트가 되도록 깊은 복사
maxV = -1
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(i, j):
    global maxV
    q = deque()
            
    q.append([i, j, 0])
    visited = [[False]*M for _ in range(N)]
    visited[i][j] = True
    while q:
        curX, curY, total = q.popleft()
                
        for x, y in move:
            nextX = curX+x
            nextY = curY+y
            if 0<=nextX<N and 0<=nextY<M and arr[nextX][nextY] == 'L' and not visited[nextX][nextY]:
                q.append([nextX, nextY, total+1])
                visited[nextX][nextY] = True
                maxV = max(total+1, maxV)
                

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            bfs(i, j)
            
                        

print(maxV)