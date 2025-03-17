import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split(" "))

arr = [list(map(int, list(input()))) for _ in range(N)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[-1]*M for _ in range(N)]

q = deque()
q.append([0, 0, 1])
visited[0][0] = 1
ans = 0

while len(q)!=0:
    curX, curY, num = q.popleft()
    if curX == N-1 and curY == M-1:
        ans = num
        break
    for x, y in move:
        nextX = curX+x
        nextY = curY+y
        if 0<=nextX<N and 0<=nextY<M and arr[nextX][nextY] == 1 and visited[nextX][nextY] == -1:
            #갈 수 있는 곳
            q.append([nextX, nextY, num+1])
            visited[nextX][nextY] = 1
print(ans)