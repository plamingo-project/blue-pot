import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for _ in range(N)]

move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
cnt = 0
time = 0

while True:
    q = deque()
    tempcnt = 0
    visited = [[False]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and not q:
                q.append([i, j])
            if arr[i][j] == 1:
                tempcnt += 1
            if arr[i][j] == 2:
                arr[i][j] = 0

    if tempcnt == 0:
        break
    
    cnt = tempcnt
    time+=1

    while q:
        curX, curY = q.popleft()
        for x, y in move:
            nextX = curX+x
            nextY = curY+y
            if 0<=nextX<N and 0<=nextY<M and not visited[nextX][nextY]:
                if arr[nextX][nextY] == 1:
                    arr[nextX][nextY] = 2
                if arr[nextX][nextY] == 0:
                    q.append([nextX, nextY])
                visited[nextX][nextY] = True

print(time)
print(cnt)